class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        maxF = 0
        res = 0
        l = 0

        #the intuition is given in a certain window, 

        for r in range(len(s)):
            #collect the count in the windows
            window[s[r]] = 1 + window.get(s[r], 0)

            maxF = max(window[s[r]], maxF) #update the maxF as needed to find the count of the most recurring

            while (r-l+1) - maxF > k:
                window[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)



        return res