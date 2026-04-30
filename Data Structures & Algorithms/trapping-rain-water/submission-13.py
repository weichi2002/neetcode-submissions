class Solution:
    def trap(self, height: List[int]) -> int:
        #min(l,r)-h[i], how much water we can trap at a given 
        leftMax = [height[0]]
        for i in range(1, len(height)):
            leftMax.append(max(leftMax[-1], height[i]))

        rightMax = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            rightMax.append(max(rightMax[-1], height[i]) )

        rightMax.reverse()

        total = 0
        for i in range(len(height)):
            volume = min(leftMax[i], rightMax[i]) - height[i]
            if volume > 0:
                total += volume
        
        return total

