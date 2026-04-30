class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##bucket sort
        freq = [[] for i in range(len(nums)+1)]
        from collections import Counter
        counter = Counter(nums)

        for n, count in counter.items():
            freq[count].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        