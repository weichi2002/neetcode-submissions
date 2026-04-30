class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #the goal is to use a hashmap
        #pass through once
        #we store the difference of diff = target - n in the hashmap and use the n as the key, whenver we encounter the diff in the nums
        #we known we seen this pair and then we retrieve the index


        hashMap = {}

        for i, val in enumerate(nums):
            
            diff = target - val

            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[val] = i
