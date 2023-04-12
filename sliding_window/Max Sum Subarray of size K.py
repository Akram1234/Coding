class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        su = 0
        maxi = float('-inf')
        i,j = 0, 0
        while j<N:
            su += Arr[j]
            if j-i+1 < K:
                j+=1
            elif j-i+1 == K:
                maxi = max(maxi, su)
                su -= Arr[i]
                i+=1
                j+=1
        return maxi
