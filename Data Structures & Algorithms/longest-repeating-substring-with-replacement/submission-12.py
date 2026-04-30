class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we want to replace the character the least occurence.
        #therefore, we should count the majority and and if any time the window - majority > k, we should incrmenet and move forward

        windows = {}     
        l = 0
        res = 0

        for r in range(len(s)):
            windows[s[r]] = 1 + windows.get(s[r], 0)
            while (r-l+1) - max(windows.values()) > k:
                windows[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        
        return res