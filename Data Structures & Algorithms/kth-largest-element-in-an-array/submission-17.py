class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap =[-x for x in nums]
        heapq.heapify(maxHeap)

        res = 0
        while k > 0:
            k -= 1
            res = heapq.heappop(maxHeap)

        return -res
            
