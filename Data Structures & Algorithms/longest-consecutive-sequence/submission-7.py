class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)

        for n in nums:
            if n-1 not in numSet: #we know its a start of a seq, helps avoid repeated work for those in the middle of a sequence
                length = 1
                while n + length in numSet:
                    length += 1
                
                maxLen = max(maxLen, length)



        return maxLen
        