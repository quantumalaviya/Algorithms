from graph import Graph

def DFS(g, k, start = 0):
    
    if start == k:
        return True
    
    stack = [start]
    n = len(g.vertices.keys())
    explored = [False]*n
    
    explored[start] = True
    
    while stack!=[]:
        curr = stack.pop()
        for i in g.vertices[curr]:
            if not explored[i]:
                if i==k:
                    return True
                stack.append(i)
                explored[i] = True
        print(curr)
    return False
        
g = Graph("u") 
g.addEdge(0,1) 
g.addEdge(0,2) 
g.addEdge(1,3) 
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)