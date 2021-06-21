class Subset:
    def __init__(self, obj):
        self.obj = obj
        self.parent = self
        self.rank = 0
        
    def Union(self, v):
        if self.rank > v.rank:
            v.parent = self
            return self.obj, v.obj
        elif v.rank > self.rank:
            self.parent = v
            return v.obj, self.obj
        else:
            v.parent = self
            self.rank+=1
            return self.obj, v.obj
    
    def findParent(self):
        if self.parent == self:
            return self
        return self.parent.findParent()

    
    

            