class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l = 0
        r = len(height)-1
        leftMax, rightMax = height[l], height[r]
        total = 0

        while l < r:
            if leftMax > rightMax:
                r-=1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        

            else:
                l+=1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]

        return total



        