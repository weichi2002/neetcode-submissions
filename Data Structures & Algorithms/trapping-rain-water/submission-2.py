class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l, r = 0, len(height)-1
        maxL, maxR = 0, 0
        total = 0

        for i in range(len(height)):
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            area = min(maxR, maxL) - height[i]
            total += area

            if maxL <= maxR:
                l += 1
            else:
                r-=1

        return total

            


        
        