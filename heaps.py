class minHeap:
    def __init__(self, arr = []):
        n = len(arr)
        self.heap = arr
        self.size = n
        for i in range(n//2-1, -1, -1):
            self.bubbleDown(i)
        
    def bubbleDown(self, i):
        l = 2*i+1
        r = l+1
        if (l>=self.size or self.heap[i]<=self.heap[l]) and (r>=self.size or self.heap[i]<= self.heap[r]):
            return None
        replace = r if self.heap[l] > self.heap[r] and r < self.size else l
        if self.heap[replace] < self.heap[i]:
            self.heap[i], self.heap[replace] = self.heap[replace], self.heap[i]
            self.bubbleDown(replace)
            
            
    def delete(self, i):
        if i<self.size-1:
            self.heap[i] = self.heap.pop()
            self.size-=1
            self.bubbleDown(i)
        
    def extractMin(self):
        if self.size == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.delete(0)
        return root
    
    def bubbleUp(self, i):
        p = (i-1)//2
        if p < 0 or self.heap[p] <= self.heap[i]:
            return None
        self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
        self.bubbleUp(p)
        
    def insert(self, k):
        self.heap.append(k)
        self.size+=1
        self.bubbleUp(self.size-1)
        
    def getMin(self):
        return self.heap[0]
        
class maxHeap:
    def __init__(self, arr = []):
        n = len(arr)
        self.heap = arr
        self.size = n
        for i in range(n//2-1, -1, -1):
            self.bubbleDown(i)
        
    def bubbleDown(self, i):
        l = 2*i + 1
        r = l+1
        if (l >= self.size or self.heap[l]<=self.heap[i]) and (r >= self.size or self.heap[r] <= self.heap[i]):
            return None
        replace = r if self.heap[l] < self.heap[r] and r < self.size else l
        if self.heap[replace] > self.heap[i]:
            self.heap[i], self.heap[replace] = self.heap[replace], self.heap[i]
            self.bubbleDown(replace)
            
    def bubbleUp(self, i):
        p = (i-1)//2
        
        if p < 0 or self.heap[p] > self.heap[i]:
            return None
        self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
        self.bubbleUp(p)
        
    def delete(self, i):
        if self.size>1:
            e = self.heap[i]
            self.size-=1
            self.heap[i] = self.heap.pop()
            self.bubbleDown(i)
        else:
            e = self.heap.pop()
        return e
    
    def extractMax(self):
        return self.delete(0)
    
    def insert(self, k):
        self.heap.append(k)
        self.size+=1
        self.bubbleUp(self.size-1)
        
    def getMax(self):
        return self.heap[0]
    
    def heapSort(self):
        arr = []
        while self.heap:
            arr.append(self.extractMax())
        return arr[::-1]
        
        
        
        
        
        