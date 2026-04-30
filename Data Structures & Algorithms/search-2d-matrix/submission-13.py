class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            row = l + (r-l)//2
            if matrix[row][0] <= target <= matrix[row][-1]:
                return self.search(matrix[row], target)
            elif matrix[row][0] < target:
                l = row + 1
            else:
                r = row - 1

        return False        

    
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False