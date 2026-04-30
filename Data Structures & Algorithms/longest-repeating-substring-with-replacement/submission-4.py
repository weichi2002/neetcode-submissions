class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #intutition
        #use l to keep track of the repeated letter
        #keep track of the longest string with the repeat

        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)
            
        return res
