class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}

        #we are counting here
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for number, count in count.items():
            freq[count].append(number)
        
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for item in freq[i]:
                ans.append(item)
            if len(ans) == k:
                return ans
            
        
    

        
    
        
        