'''
for w = 0 to W do 
   c[0, w] = 0 
for i = 1 to n do 
   c[i, 0] = 0 
   for w = 1 to W do 
      if wi ≤ w then 
         if vi + c[i-1, w-wi] then 
            c[i, w] = vi + c[i-1, w-wi] 
         else c[i, w] = c[i-1, w] 
      else 
         c[i, w] = c[i-1, w] 
'''

def knapsack(weights, profits, kp):
    n = len(weights)
    dp = []
    for i in range(n+1):
        dp.append([0]*(kp+1))
        
        
    for i in range(1, n+1):
        for w in range(1, kp+1):
            if weights[i-1] <= w:
                dp[i][w] = max(profits[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    print(dp[-1][-1])
    
weights = [30,50,10]
val = [600,500,200]
cap = 60
knapsack(weights, val, cap)