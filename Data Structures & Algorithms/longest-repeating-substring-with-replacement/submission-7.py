class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #we want ot replace the least occuring character
        #use a dictionary to keep track of count of character
        #we want to keep track of the length by r-l+1, thats length
        #we want to update the window whenever max(count) equals the k value 
        #when we update, we want to increment the l value by 1 and remove 1 in the dict

        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)

        return res