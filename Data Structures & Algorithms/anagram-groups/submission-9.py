class Solution:                         
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        visited = [False] * len(strs)
        res = []
        
        for i in range(len(strs)):
            if visited[i]: continue
            temp = [strs[i]]
            for j in range(i+1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    visited[j] = True
            res.append(temp)

        return res 



    
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2): return False
        from collections import Counter
        return Counter(s1) == Counter(s2)
