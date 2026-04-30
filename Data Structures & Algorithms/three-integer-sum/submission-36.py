class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums)-2):

            if i > 0 and nums[i-1] == nums[i]: continue

            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[r] + nums[l]

                if total == 0:
                    res.append([nums[i] , nums[r] , nums[l]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif total < 0:
                    l+=1
                else:
                    r-=1

        return res

        