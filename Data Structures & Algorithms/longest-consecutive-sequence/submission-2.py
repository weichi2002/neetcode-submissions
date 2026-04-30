class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if n-1 not in numSet:
                temp = 1
                while n + 1 in numSet:
                    temp+=1
                    n = n + 1
                longest = max(longest, temp)
        
        return longest
        