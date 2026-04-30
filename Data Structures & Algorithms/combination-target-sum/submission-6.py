class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()
        cur = []

        def dfs(i):
            if sum(cur) == target:
                res.append(cur.copy())
                return 
            
            for j in range(i, len(nums)):
                if sum(cur) + nums[j] > target:
                    return 
                
                cur.append(nums[j])
                dfs(j)
                cur.pop()
        
        dfs(0)
        return res
                
