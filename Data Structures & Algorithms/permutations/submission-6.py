class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]

        for n in nums:
            temp = []
            for p in perms:
                for i in range(len(p)+1):
                    copy = p.copy()
                    copy.insert(i, n)
                    temp.append(copy)

            perms = temp


        return perms
        