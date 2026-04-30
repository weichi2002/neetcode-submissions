class Solution:
    def trap(self, height: List[int]) -> int:
        #water is bounded by he left tallest and the right tallest
        #the min(l,r ) - hieght[i]
        #and we dont want to add negative water
        #so lets compute left and rightMax in array

        total = 0
        leftMax = [height[0]]
        for i in range(1, len(height)):
            leftMax.append(max(height[i], leftMax[-1]))

        rightMax = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            rightMax.append(max(height[i], rightMax[-1]))

        rightMax.reverse()

        for i in range(len(height)):
            vol = min(leftMax[i], rightMax[i]) - height[i]
            if vol > 0: 
                total += vol



        return total