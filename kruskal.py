from unionFind import Subset
from graph import Graph

g = Graph("d")
g.addEdge(0,1,3)
g.addEdge(1,2,4)
g.addEdge(2,3,4)
g.addEdge(0,2,10)
g.addEdge(0,3,5)


class Edge:
    def __init__(self, e, l):
        self.l = l
        self.e = e
        
    def __repr__(self):
        return str(self.e) + "-" + str(self.l)
    
E = list(g.edges.keys())   
start = E[0]
mst = []

edges = [Edge(start, g.edges[start])]

for e in E[1:]:
    i = 0
    l = g.edges[e]
    while i < len(edges) and edges[i].l > l:
        i+=1
    edges.insert(i, Edge(e, l))
    
    
subset = []
for i in g.vertices.keys():
    subset.append(Subset(i))
    
while edges:
    e = edges.pop()
    u,v = e.e
    if subset[u].findParent() != subset[v].findParent():
        subset[u].Union(subset[v])
        mst.append((u,v))

print(mst)