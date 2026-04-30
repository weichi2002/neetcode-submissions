class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        #bucket sort in reverse
        freq = [[] for i in range((len(nums)+1))]

        for n, count in count.items():
            freq[count].append(n)

        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
        

        




