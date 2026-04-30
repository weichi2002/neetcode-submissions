class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i < j:
            res = numbers[i] + numbers[j]
            if res == target:
                return [i+1, j+1]
            if res < target:
                i+= 1
            else:
                j-=1



        #return 1st index solution in the array
        #cannot be the element
