class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #lets do the brute force way, calcualte iterate thhru and skip the cur index

        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            res.append(product)

        return res
                
        