from graph import Graph
from queue import Queue

def BFS(g, start = 0):
    n = len(g.vertices.keys())
    q = Queue(n)
    explored = [False]*n
    q.put(start)
    explored[start] = True
    while not q.empty():
        curr = q.get()
        for i in g.vertices[curr]:
            if not explored[i]:
                q.put(i)
                explored[i] = True
        print(curr)
        
g = Graph()
g.addEdge(0,1) 
g.addEdge(0,2) 
g.addEdge(1,3) 
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)
            
BFS(g)
        