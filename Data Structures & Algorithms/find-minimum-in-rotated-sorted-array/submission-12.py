class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums)-1

        while l <= r:
            #figure out if sorted at first
            if nums[l] < nums[r]:
                return min(res, nums[l])

            #not sorted, we start figuring out which part to search
            m = (r+l)//2
            res = min(res, nums[m])
            if nums[l] <= nums[m]: #left portion is sorted, look on the right
                l = m + 1
            else:
                r = m - 1
        
        return res



        