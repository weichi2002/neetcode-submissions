class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""
        #some sort of sliding window
        l = 0
        res, resLen = "", float("inf")

        #we want to use dictionary to count
        from collections import Counter
        countT = Counter(t)

        #we have to track that the windows contains the right element. But they wont be equal to each other
        #we should have a couunt mechanism

        matches = 0

        window = {}

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                matches += 1
            
            while matches == len(countT):
                #capture and attempt to shrink the window
                if (r-l+1) < resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                #shrink the window
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    matches-=1
                l+=1

        return res if resLen != float('inf') else ""
        