class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #start with left pointer and right pointer
        #if we see 0, swap it with L and increment
        #if we see 2, swap with right and decrement r, but we dont shift the current pointer forward because we dont know what we just swapped is correct, so we check again

        l = 0
        r = len(nums)-1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l+=1
            elif nums[i] == 2:
                swap(i, r)
                r-=1
                #should not decrement
                i-=1
            i+=1
        

        