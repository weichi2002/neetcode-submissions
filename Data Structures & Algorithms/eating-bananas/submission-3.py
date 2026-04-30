class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            totalTime = 0
            speed = (l+r)//2
            for p in piles:
                totalTime += math.ceil(p/speed)
            if totalTime <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        
        return res
