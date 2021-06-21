from collections import defaultdict

class Graph():
    def __init__(self, status = "ud"):
        self.vertices = defaultdict(list)
        self.edges = {}
        self.status = status
        
    def addEdge(self, u, v, l = 1):
        self.vertices[u].append(v)
        if self.status == "ud":
            self.vertices[v].append(u)
        elif v not in self.vertices:
            self.vertices[v] = []
        self.edges[(u,v)] = l
        
    def copy(self):
        g = Graph()
        g.vertices = self.vertices.copy()
        g.edges = self.edges.copy()
        
        return g