class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        
        numsCount = Counter(nums)
        
        maj = 0
        highestCount = 0
        for n, count in numsCount.items():
            if count > highestCount:
                highestCount = count
                maj = n
        
        return maj


        