class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)-1
        while l <= r:
            row = l + (r-l)//2
            if matrix[row][0] <= target <= matrix[row][-1]:
                return self.binary_search(matrix[row], target)
            elif matrix[row][0] > target:
                r = row - 1
            else:
                l = row + 1
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

