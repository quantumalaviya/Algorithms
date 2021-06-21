from graph import Graph

g = Graph("d")
g.addEdge(0,1,3)
g.addEdge(1,2,4)
g.addEdge(2,3,4)
g.addEdge(0,2,-10)
g.addEdge(0,3,5)


def BF(g, start = 0):
    n = len(g.vertices.keys())
    A = []
    for i in range(n):
        A.append([float("inf")]*n)
        
    A[0][start] = 0
    
    for i in range(1, n):
        for v in g.vertices.keys():
            A[i][v] = A[i-1][v]
            
            for e in g.edges.keys():
                if e[1] == v:
                    m = A[i-1][e[0]] + g.edges[e]
                    if m < A[i][v]:
                        A[i][v] = m
    
    if A[-2] == A[-1]:
        return A[-1]
    
    
        
        
        


