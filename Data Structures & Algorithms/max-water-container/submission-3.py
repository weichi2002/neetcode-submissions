class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we use two poitners
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            vol = (r-l) * min(heights[r], heights[l])
            res = max(res, vol)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1

            #how do we determine which side to move, 
            #they are not sorted, depends on which side is higher
        return res