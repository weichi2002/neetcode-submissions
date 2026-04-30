class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = min(l, r) * (r-l+1)
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            volume = min(heights[l], heights[r]) * (r-l)
            res = max(res,volume)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l+=1


        return res