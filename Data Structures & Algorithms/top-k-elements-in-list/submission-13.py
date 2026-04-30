class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #we want to use bucketsort
        freq = [[] for _ in range(len(nums)+1)]

        #we want to count the frequency 
        from collections import Counter
        count = Counter(nums)

        for num, times in count.items():
            freq[times].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

        


        

        #reverse and append until len(res) == k