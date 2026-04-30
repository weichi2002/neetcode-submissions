class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        #we want to maintain a window that check if the letter count is exactly the same in the region

        c1 = Counter(s1)
        
        window = Counter()

        for i, c in enumerate(s2):
            window[c] += 1

            if i >= len(s1):
                leftChar = s2[i-len(s1)]
                window[leftChar] -= 1
                if window[leftChar] == 0:
                    del window[leftChar]
            
            if window == c1: return True
        
        return False

