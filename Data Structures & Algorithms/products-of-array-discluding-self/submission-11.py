class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        post = [0] * n

        pref[0] = 1
        post[-1] = 1

        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        
        for i in range(n-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]
        
        for i in range(n):
            res[i] = pref[i] * post[i]
        
        return res