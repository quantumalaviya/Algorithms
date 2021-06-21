from graph import Graph

g = Graph("u") 
g.addEdge(7,5) 
g.addEdge(7,6) 
g.addEdge(6,4) 
g.addEdge(5,4) 
g.addEdge(5,2)
g.addEdge(6,3) 
g.addEdge(3,1) 
g.addEdge(2,1)
g.addEdge(1,0)

n = len(g.vertices.keys())
explored = [False]*n
labels = [0]*n
label = n

def DFS(g, start):
    global label
    explored[start] = True
    print(start)
    for i in g.vertices[start]:
        if not explored[i]:
            DFS(g, i)
    
    labels[start] = label
    label-=1
    
def topologicalSort(g):
    for i in range(n-1, -1, -1):
        if not explored[i]:
            DFS(g, i)
                      
topologicalSort(g)  