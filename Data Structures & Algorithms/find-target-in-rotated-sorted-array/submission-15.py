class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: #left is sorted, we have a range to work with
                if target < nums[l] or target > nums[m]:
                    l = m + 1 
                else:
                    r = m - 1
            else: #right side is sorted
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1





        
        return -1