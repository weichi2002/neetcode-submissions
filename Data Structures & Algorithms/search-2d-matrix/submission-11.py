class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1

        while start <= end:
            row = start + (end-start)//2
            if matrix[row][0] <= target <= matrix[row][-1]:
                return self.helper(matrix[row], target)
            elif matrix[row][0] > target:
                end = row-1
            else:
                start = row+1
        
        return False


        
    def helper(self, array, target):

        l = 0
        r = len(array)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return False

