class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        #we want to find the maximum length which we can get by replacing k character
        #we alway want to find the minimum that it would take to repalce
        # we can derive the formula for the window like this: r-l+1 - max(count.values()) >= k

        count = {}
        l = 0
        maxLen = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            maxLen = max(maxLen, r-l+1)
        return maxLen
            