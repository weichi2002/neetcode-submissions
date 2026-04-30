class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #water contianer height is restricted by the min(left, right) * (r-l)+1

        l = 0
        r = len(heights)-1

        
        res = 0

        while l < r:
            container = min(heights[l], heights[r]) * (r-l)
            res = max(res, container)

            if heights[l] < heights[r]:
                l+=1
            
            else:
                r-=1

            
        return res

        