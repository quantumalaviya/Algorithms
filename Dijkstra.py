from graph import Graph
  
g = Graph("d")
g.addEdge(0,1,1)
g.addEdge(1,2,2)
g.addEdge(2,3,5)
g.addEdge(0,2,3)
g.addEdge(0,3,4)

class nodeHeap:
    def __init__(self, v, score):
        self.v = v
        self.score = score
    
    def __repr__(self):
        return str(self.v) + "->" + str(self.score)
        
def bubbleDown(arr, i):
    l = 2*i + 1
    r = l + 1
    n = len(arr)
    if (l >= n or arr[l].score>arr[i].score) and (r >= n or arr[r].score>arr[i].score):
        return
    replace = r if r<n and arr[l].score > arr[r].score else l
    if arr[replace].score < arr[i].score:
        arr[replace], arr[i] = arr[i], arr[replace]
        bubbleDown(arr, replace)
        
def bubbleUp(arr, i):
    p = (i-1)//2
    if p>=0 and arr[p].score > arr[i].score:
        arr[p], arr[i] = arr[i], arr[p]
        bubbleUp(arr, p)
        
def delete(arr, k):
    i = -1
    while i < len(arr)-1:
        i+=1
        if arr[i].v == k:
            break
    temp = arr[i]
    arr[i], arr[-1] = arr[-1], arr[i]
    if len(arr)>=1:
        arr.pop()
        bubbleDown(arr, i)
    else:
        arr = []
    return temp
        
def insert(arr, node):
    arr.append(node)
    bubbleUp(arr, len(arr) - 1)
    
def extractMin(arr):
    temp = arr[0]
    delete(arr, arr[0].v)
    return temp
    
def c(k, arr):
    for i in arr:
        if i.v == k:
            return True
    return False

def dijkstra(g, start = 0):
    edges = g.edges
    X = set([start])
    V = set(g.vertices.keys())
    A = [0] * len(V)

    heap = []
    for i in g.vertices[start]:
        heap.append(nodeHeap(i, edges[(start, i)]))
        
    n = len(heap)
    for i in range(n//2 - 1, -1, -1):
        bubbleDown(heap, i)
        
    while X!=V:
        w = extractMin(heap)
        A[w.v] += w.score
        X.add(w.v)
        w = w.v
        
        for i in g.vertices[w]:
            if c(i, heap):
                temp1 = delete(heap, i).score
                temp2 = A[w] + edges[(w, i)]
                score = min(temp1, temp2)
                insert(heap, nodeHeap(i, score))
            else:
                insert(heap, nodeHeap(i, A[w] + edges[(w, i)]))
                
    return A
                
print(dijkstra(g))     