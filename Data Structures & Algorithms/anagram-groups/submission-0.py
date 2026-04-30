class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        while len(strs) > 0:
            word = strs[0]
            temp = [word]
            strs.pop(0)
            toPop = []
            for i in range(len(strs)):
                if self.isAnagram(word, strs[i]):
                    temp.append(strs[i])
                    toPop.append(i)
            print(strs)
            print(temp)
            print(toPop)
            ans.append(temp)
            for item in reversed(toPop):
                strs.pop(item)
        
        return ans

    
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2): return False
        return sorted(s1) == sorted(s2)
        
        