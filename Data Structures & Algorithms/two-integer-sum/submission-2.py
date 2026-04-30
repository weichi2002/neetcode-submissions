class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        #use dictionary to store the index where we have seen the number
        #to figure out if they sum up to target, we subtract them and search in dictionary

        for i, val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [d[diff], i]
            
            d[val] = i #store the value