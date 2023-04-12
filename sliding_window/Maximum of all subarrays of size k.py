class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        res = []
        li = []
        i,j = 0,0 
        while j<n:
            while li and li[-1] < arr[j]:
                li.pop()
            li.append(arr[j])
            
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                res.append(li[0])
                if arr[i]==li[0]:
                    li.pop(0)
                i+=1
                j+=1
        return res
