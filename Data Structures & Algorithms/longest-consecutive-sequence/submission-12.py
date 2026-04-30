class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #transform num in a set:
        #naively we could run o(1) and compare every sequence starting at each number adn try for min length
        #we could avoid that if we only start at beginng of the seq
        #we knwo the number is a start if number-1 dne in nums

        numSet = set(nums)
        maxLen = 0

        for n in nums:
            length = 1
            if n-1 not in numSet:
                while n + length in numSet:
                    length += 1
            maxLen = max(maxLen, length)
            
        return maxLen

        
        