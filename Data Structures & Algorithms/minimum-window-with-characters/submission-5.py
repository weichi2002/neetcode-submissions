class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        #use a dictionary to keep track of counts
        from collections import Counter
        countT = Counter(t)
        window = {}

        have, need = 0, len(countT) #use this track of tje matches we get, if get match, we try to shrink the window

        res, resLen = "", float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                #we have a window now
                if (r - l + 1) < resLen:
                    resLen = (r-l+1)
                    res = s[l: r+1]
                
                #shrink the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
                

        return res if resLen != float('inf') else ""
        