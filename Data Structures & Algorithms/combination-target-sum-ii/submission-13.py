class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i == len(candidates):
                return 

            #include
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: #skip duplicates liek three sum
                i+=1
            dfs(i+1, curr, total)

        
            #skip

        dfs(0, [], 0)
        
        return res

        

        