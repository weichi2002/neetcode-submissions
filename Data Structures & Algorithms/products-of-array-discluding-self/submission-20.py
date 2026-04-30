class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #lets do the brute force way, calcualte iterate thhru and skip the cur index
        #break this down and think about how we can handle
        #can get left excluding and right exclduign

        #actually optimize this to save on the space

        prefix = 1
        postfix = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res


        
                
        