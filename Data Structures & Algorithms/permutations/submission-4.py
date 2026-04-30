class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            newPerm = []
            for p in perms:
                for i in range(len(p)+1):
                    copy = p.copy()
                    copy.insert(i, n)
                    newPerm.append(copy)
            perms = newPerm
        
        return perms