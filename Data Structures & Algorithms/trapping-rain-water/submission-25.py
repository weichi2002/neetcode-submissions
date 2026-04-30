class Solution:
    def trap(self, height: List[int]) -> int:
        #the intution is to find the minimum of left or right sid
        #and we want to use the left max or rightmax known according to the boundary
        #the volume is thus calculated by min(maxleft, maxright)


        leftMax = [height[0]]
        for i in range(1, len(height)):
            leftMax.append(max(leftMax[-1], height[i]))
        
        rightMax = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            rightMax.append(max(rightMax[-1], height[i]))

        rightMax.reverse()

        #now we iterate throught and construct, omit the negative
        res = 0
        for i in range(len(height)):
            area = min(leftMax[i], rightMax[i]) - height[i]
            if area > 0:
                res += area
        return res