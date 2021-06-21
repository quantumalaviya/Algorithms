from graph import Graph

g = Graph("d")
g.addEdge(0,1,3)
g.addEdge(1,2,4)
g.addEdge(2,3,4)
g.addEdge(0,2,10)
g.addEdge(0,3,5)

def FW(g):
    V = g.vertices.keys()
    n = len(V)
    
    A = [[[ 0 for i in range(n)] for k in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j: 
                A[0][i][j] = 0
            elif (i,j) in g.edges:
                A[0][i][j] = g.edges[(i,j)]
            else:
                A[0][i][j] = float("inf")
     
                
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k] + A[k-1][k][j])
    
    
    return A[-1]
    