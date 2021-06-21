from graph import Graph

def DFS(g, start = 0):
    explored[start] = True
    print(start)
    for i in g.vertices[start]:
        if not explored[i]:
            DFS(g, i)
            
g = Graph("u") 
g.addEdge(0,1) 
g.addEdge(0,2) 
g.addEdge(1,3) 
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)
explored = [False]*len((g.vertices.items()))

DFS(g)