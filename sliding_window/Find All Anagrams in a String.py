class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pMap = {}
        for ch in p:
            pMap[ch] = pMap.get(ch, 0) + 1
        
        count = len(pMap)

        i, j = 0, 0
        ans = []
        k,n = len(p), len(s)
        while j < n:
            if s[j] in pMap:
                pMap[s[j]]-=1
                if pMap[s[j]] == 0:
                    count -= 1
            if j-i+1 < k:
                j+=1
            elif j-i+1 == k:
                if count == 0:
                    ans.append(i)
                if s[i] in pMap:
                    if pMap[s[i]] == 0:
                        count += 1
                    pMap[s[i]] += 1
                i+=1
                j+=1
        return ans


