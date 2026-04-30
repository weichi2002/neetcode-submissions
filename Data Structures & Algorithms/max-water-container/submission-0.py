class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        maxSize = 0
        while l < r:
            storage = (r-l) * min(heights[r], heights[l])
            maxSize = max(storage, maxSize)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return maxSize
            

        