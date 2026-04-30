class Solution:
    def trap(self, height: List[int]) -> int:
        #we can optimize the space of this, just by using a two pointer
        #instead of o(n), we get o(1)  
        if len(height) < 3: return 0 

        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        total = 0

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]

            else:
                r-=1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
    
        return total