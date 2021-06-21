def merge(arr1, arr2, m, n):
    merged = []
    i = j = count = 0
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            count+=(m-i)
            j+=1
        
    while i < m:
        merged.append(arr1[i])
        i+=1
            
    while j < n:
        merged.append(arr2[j])
        j+=1
           
    return merged, count

def sort(arr, n):
    if n == 1:
        return arr, 0
    mid = n//2
    A, X = sort(arr[:mid], mid)
    B, Y = sort(arr[mid:], n-mid)
    C, Z = merge(A, B, mid, n-mid)
    
    return C, X+Y+Z