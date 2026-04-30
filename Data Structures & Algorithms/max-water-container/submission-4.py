class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we wanna maximize the amount we can get
        #vol = min(l, r) * (r-l)
        l = 0
        r = len(heights)-1
        maxVol = 0

        while l < r:
            vol = min(heights[l], heights[r]) *  (r-l)
            maxVol = max(maxVol, vol)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return maxVol
