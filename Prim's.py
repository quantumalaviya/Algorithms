from collections import defaultdict

class Graph():
    def __init__(self):
        self.vertices = defaultdict(list)
        self.edges = {}
        
    def addEdge(self, u, v, l = 1):
        self.vertices[u].append(v)
        self.vertices[v] = [] # treating as directed graph
        self.edges[(u,v)] = l

class nodeHeap:
    def __init__(self, v, score):
        self.v = v
        self.score = score
        
def bubbleDown(arr, i):
    lowest = i
    l = 2 * i + 1
    r = 2 * i + 2
    n = len(arr)
        
    if l < n and arr[lowest].score > arr[l].score:
        lowest = l
        
    if r < n and arr[lowest].score > arr[r].score:
        lowest = r
            
    if lowest != i:
        arr[i].score, arr[lowest].score = arr[lowest].score, arr[i].score
        bubbleDown(arr, lowest)
        
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
    
def checker(k, arr):
    for i in arr:
        if i.v[1] == k:
            return i.v, True
    return None, False

def prim(g, start = 0):
    edges = g.edges
    X = set([start])
    V = set(g.vertices.keys())
    T = []

    heap = []
    for i in g.vertices[start]:
        heap.append(nodeHeap((start, i), edges[(start, i)]))
        
    n = len(heap)
    for i in range(n//2 - 1, -1, -1):
        bubbleDown(heap, i)
        
    while X!=V:
        e = extractMin(heap)
        if e.v[1] not in X:
            T.append(e.v)
        X.add(e.v[1])
        w = e.v[1]
        
        for i in g.vertices[w]:
            u,check = checker(i, heap)
            if check:
                temp1 = delete(heap, u).score
                temp2 = edges[(w, i)]
                score = min(temp1, temp2)
                
                if score == temp1:
                    insert(heap, nodeHeap(u, score))
                else:
                    insert(heap, nodeHeap((w,i), score))
            else:
                insert(heap, nodeHeap((w,i), edges[(w, i)]))
                
    return T  

g = Graph()
g.addEdge(0,1,4)
g.addEdge(1,2,3)
g.addEdge(2,3,6)
g.addEdge(3,4,7)
g.addEdge(0,4,5)
g.addEdge(1,4,1)
g.addEdge(1,3,6)
g.addEdge(2,4,2)

print(prim(g))