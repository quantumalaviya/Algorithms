M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

n = len(M)

for i in range((n+1)//2):
    x = n - i - 1
    for j in range(i, n - 1):
        print((i, j),(j, x), (x, x-j+i), (x-j+i, i))
        M[i][j], M[j][x], M[x][x-j+i], M[x-j+i][i] = M[x-j+i][i], M[i][j], M[j][x], M[x][x-j+i]
        
print(M)