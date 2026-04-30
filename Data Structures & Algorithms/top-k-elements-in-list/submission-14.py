class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]

        from collections import Counter

        numCount = Counter(nums)

        for number, count in numCount.items():
            freq[count].append(number)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res


        
        