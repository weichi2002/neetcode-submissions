class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)

        for m in matrix:
            if m[0] <= target <= m[-1]:
                return self.binary_search(m, target)
        
        return False


    
    def binary_search(self, nums, target):
        l = 0
        r = len(nums)

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

