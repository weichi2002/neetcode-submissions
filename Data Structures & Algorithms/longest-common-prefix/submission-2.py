class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        #how to iterate letter by 
        for i in range(len(strs[0])):
            for s in strs: #iterate every character, what if s goes out of bound
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res

