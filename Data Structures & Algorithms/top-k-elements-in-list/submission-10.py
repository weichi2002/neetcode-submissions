class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we want to return the top k most frequent 
        #use a dicitonary to count, hashmap
        #we can apply bucketsort to this problem
        freq = [[] for _ in range(len(nums)+1)]

        from collections import Counter
        count = Counter(nums)

        for i, c in count.items():
            freq[c].append(i)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res

        #add the top k most to the res array and return 



        return res

        