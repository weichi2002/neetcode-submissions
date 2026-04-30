class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use some sort of the ds to keep track of what we have repeat
        #variable to hold the longest length
        #r-l

        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
            res = max(r-l+1, res)


        return res