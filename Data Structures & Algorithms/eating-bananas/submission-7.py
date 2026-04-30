class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        #know that the max speed is the biggest number in the piles
        r = max(piles)
        res = len(piles)

        while l <= r:
            speed = l + (r-l)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/speed)
            
            if totalTime <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1

        return res
