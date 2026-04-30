class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #get the frequency, sort it backward from most frequent

        count = Counter(nums)

        freq = [[] for i in range (len(nums)+1)] #each  index at the bucket, will represent ferquency that the numner occurs
        
        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq)-1, -1, -1):

            for num in freq[i]: #this will only execute if freq[i] is non empty
                res.append(num)
                if len(res) == k:
                    return res
