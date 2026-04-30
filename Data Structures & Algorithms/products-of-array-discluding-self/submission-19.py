class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #lets do the brute force way, calcualte iterate thhru and skip the cur index
        #break this down and think about how we can handle
        #can get left excluding and right exclduign

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
            
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        
        return res
        
                
        