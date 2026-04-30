class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d1:
                return [d1[diff], i]
            d1[nums[i]] = i
        