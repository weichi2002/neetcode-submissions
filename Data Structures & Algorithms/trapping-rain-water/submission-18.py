class Solution:
    def trap(self, height: List[int]) -> int:
        #intuitot: min(height[r], height[l]) - height[i]
        #but for the water bounded more than a grid, we want to consider the left tallest, and likewise for the right
        #for negative volume, we skip because cant have neagtive
        #construct array tracking leftMax and rightMax
        #iterate thru the array to compute at given index, what volume of water you can get

        res = 0
        n = len(height)
        l, r = 0, n-1 

        leftMax = [height[l]] * n
        for i in range(1, n-1):
            leftMax[i] = max(leftMax[i-1], height[i])
                
        rightMax = [height[r]] * n
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        
        for i in range(n):
            vol = min(leftMax[i], rightMax[i]) - height[i]
            if vol > 0:
                res += vol

        return res

        