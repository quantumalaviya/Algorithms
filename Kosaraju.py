from graph import Graph

def reverse(g):
    grev = Graph("u")
    for i in g.vertices:
        for j in g.vertices[i]:
            grev.addEdge(j, i)
    return grev

g = Graph("u") 
g.addEdge(0,1) 
g.addEdge(1,2) 
g.addEdge(2,3) 
g.addEdge(3,0) 
g.addEdge(1,4)

t = 0
s = None
leaders = list(g.vertices.keys())
times = {}

def DFS(g, i):
    global s, t, times, leaders, explored
    explored[i] = True
    leaders[i] = s
    
    for edge in g.vertices[i]:
        if not explored[edge]:
            DFS(g, edge)
            
    t+=1
    times[t] = i

def Kosaraju1(g):
    n = len(g.vertices.keys())
    global explored
    explored = [False]*n
    
    for i in range(n-1, -1, -1):
        if not explored[i]:
            DFS(g, i)
            
def Kosaraju2(g):
    global s
    n = len(g.vertices.keys())
    global explored
    explored = [False]*n
    
    for _ in range(n, 0, -1):
        i = times[_]
        if not explored[i]:
            s = i
            DFS(g, i)
            
Kosaraju1(reverse(g))
Kosaraju2(g)            
            
            