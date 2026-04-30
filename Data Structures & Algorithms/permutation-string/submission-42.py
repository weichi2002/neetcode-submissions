class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        window = Counter()
        c1 = Counter(s1)

        for r in range(len(s2)):
            
            
            window[s2[r]] += 1

            if r >= len(s1):   
                leftChar = s2[r-len(s1)]
                window[leftChar] -= 1
                if window[leftChar] == 0:
                    del window[leftChar]

            if window == c1:
                return True
        return False
        



