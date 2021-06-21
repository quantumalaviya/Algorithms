from unionFind import Subset
from graph import Graph
import random

def Karger(g):
    subset = [] #holds v as subset objects
    edges = list(g.edges.keys()) #holds edges connecting v
    for v in g.vertices.keys():
        subset.append(Subset(v)) 
    
    discard = 0
    
    while len(subset)-discard>2:
        i = random.randint(0, len(edges)-1)
        edge = edges[i]
        del edges[i]
        print(edge)
        u, v = edge
        
        p, c = subset[u].Union(subset[v])
        discard+=1
        for i, x in enumerate(edges):
            if c in x:
                edges[i] = tuple(sorted((p, x[0] if x[1]==c else x[1])))
        print(subset, edges)
        
        ans = []
        for i in edges:
            if i!=tuple([i[0]]*2):
                ans.append(i)
                
    return ans


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,3)
g.addEdge(1,2)
            
