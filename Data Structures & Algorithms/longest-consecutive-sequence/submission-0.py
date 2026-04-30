class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        maxLen = 0
        for n in nums:
            temp = 1
            while n + 1 in num_set:
                n += 1
                temp += 1

            if temp > maxLen:
                maxLen = temp
        
        return maxLen
            
            
                
        