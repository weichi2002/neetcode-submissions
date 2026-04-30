class Solution:
    def trap(self, height: List[int]) -> int:
        #water is bounded by he left tallest and the right tallest
        #the min(l,r ) - hieght[i]
        #and we dont want to add negative water
        #so lets compute left and rightMax in array

        #we are use o(n) space
        #we want to save on the space
        #then we can use two pointer appraoch and adjust the index smartly to track the leftMax and rightMax so we dont have to keep track of them in the array

        total = 0
        l = 0
        r = len(height)-1
        leftMax = height[0]
        rightMax = height[-1]

        while l < r:
            if leftMax < rightMax:
                #here we know we want to take the height from left bc is smaller
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                #we want to compute the next index
                r -= 1
                rightMax = max(rightMax, height[r]) #we also want to update before hand to avoid gettting negative
                #ex 2, 4  choose 2 -> -2, if we choose 4-- > 0
                total += rightMax - height[r]


        return total