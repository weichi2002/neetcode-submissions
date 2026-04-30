class Solution:
    def trap(self, height: List[int]) -> int:
        #intuitot: min(height[r], height[l]) - height[i]
        #but for the water bounded more than a grid, we want to consider the left tallest, and likewise for the right
        #for negative volume, we skip because cant have neagtive
        #construct array tracking leftMax and rightMax
        #iterate thru the array to compute at given index, what volume of water you can get

        #now we want to optimize this, by using O1 space
        #use two poitner instaed
        res = 0
        n = len(height)
        l, r = 0, n-1 
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]

            else:
                r-=1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
        
        #this works because we know that its computed by whichever side is smaller
        #and the water is bounded by the max that we know on the left
        # we increment the index before we update maxHeight because we dont want to run into negative
        # so the res wills give zero for negative and we still keep the largeest max if that wasnt the case
        return res

        