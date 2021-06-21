from queue import Queue
from graph import Graph

def BFS(g, k, start = 0):
    if start == k:
        return True
    n = len(g.vertices.keys())
    q = Queue(n)
    explored = [False]*n
    
    q.put(start)
    explored[start] = True
    
    while not q.empty():
        curr = q.get()
        for v in g.vertices[curr]:
            if not explored[v]:
                if v == k:
                    return True
                q.put(v)
                explored[v] = True
    return False
                
g = Graph()
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,3)
g.addEdge(1,2)
            
        
                
    
    