import numpy as np

class item:
    def __init__(self, cost, i):
        self.cost = cost
        self.item = i
    
    def __repr__(self):
        return str(self.cost) + " " + str(self.item)


def bubbleDown(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
                
    if l < n and arr[largest].cost < arr[l].cost:
        largest = l
         

    if r < n and arr[largest].cost < arr[r].cost:
        largest = r
         
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        bubbleDown(arr, n, largest)
    
def knapsack(weights, profits, kp):
    temp = np.array(profits)/np.array(weights)
    n = len(temp)
    ans = [None]*n
    cost = []
    for i in range(n):
        cost.append(item(temp[i], i))
       
    for i in range(n//2 - 1, -1, -1):
        bubbleDown(cost, n, i)
    
    while cost and kp>0:
        if weights[cost[0].item]>kp:
            ans[cost[0].item] = kp/weights[cost[0].item]
            kp = 0
        else:
            ans[cost[0].item] = 1
            kp-= weights[cost[0].item]
        cost[0], cost[-1] = cost[-1], cost[0]
        cost = cost[:-1]
        bubbleDown(cost, len(cost), 0)
        
    return ans
    
weights = [30,50,10]
val = [600,500,200]
capacity = 60

print(knapsack(weights, val, capacity))