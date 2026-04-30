class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##bucket sort
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, count in count.items():
            freq[count].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        