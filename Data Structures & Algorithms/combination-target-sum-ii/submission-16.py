class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtrack(i, total, combo):
            if total == target:
                res.append(combo.copy())
                return 

            if total > target or i == len(candidates):
                return
            
            combo.append(candidates[i])
            backtrack(i+1, total + candidates[i], combo)
            combo.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: #this is to leave space in the front
                i+=1
            backtrack(i+1, total, combo)

        backtrack(0, 0, [])
        return res
        