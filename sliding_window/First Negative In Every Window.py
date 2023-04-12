def firstNegative(arr, n, k) :
    ans = []
    l = []
    i,j = 0, 0
    while j < len(arr):
        if arr[j] < 0:
            l.append(arr[j])
        
        if j-i+1 < k:
            j+=1
        elif j-i+1==k:
            if not l:
                ans.append(0)
            else:
                ans.append(l[0])
            if arr[i] < 0:
                l.pop(0)
            i+=1
            j+=1
    
    return ans


