class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #stop when there is a mismatch or out of bound
        res = ""

        #hypothetically we start with the first string
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res 
        