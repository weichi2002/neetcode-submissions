class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort but we cant do that

        #transform this into a hashset

        #we know its a start of a sequnce, if n-1 doesnt exist in the set

        if not nums: return 0

        numSet = set(nums)

        res = 0
        for n in nums:
            length = 1
            if n - 1 not in numSet:
                j = n
                while j + 1 in numSet:
                    j += 1
                    length += 1
                
            res = max(res, length)
        
        return res

