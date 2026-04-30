class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = numbers
        l = 0
        r = len(n)-1

        for i in range(len(n)-1):
            res = n[l] + n[r]
            if res == target:
                return [l+1, r+1]
            elif res < target:
                l+=1
            else:
                r-=1



        