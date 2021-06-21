def karatsuba(x, y):
    
    n = len(str(x))
    if n==1:
        ans = 0
        for i in range(y):
            ans+=x
            
        return ans
    
    a = int(str(x)[:int(n/2)])
    b = int(str(x)[int(n/2):])
    
    c = int(str(y)[:int(n/2)])
    d = int(str(y)[int(n/2):])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pro =  (a+b) * (c+d) - ac - bd
    
    fin = (10**n)*ac + (10**(int(n/2)))*pro + bd
    
    return fin
    