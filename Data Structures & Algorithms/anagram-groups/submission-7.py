class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        while len(strs) != 0:
            temp = [strs.pop()]
            for i in range(len(strs)-1, -1, -1):
                if self.isAnagram(temp[0], strs[i]):
                    temp.append(strs.pop(i))
            ans.append(temp)

        return ans


    
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2): return False
        return sorted(s1) == sorted(s2)
        
        