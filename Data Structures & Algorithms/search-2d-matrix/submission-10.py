class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for r in matrix:
            if r[0] <=  target <= r[-1]:
                return self.helper(r, target)

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

