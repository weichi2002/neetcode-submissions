class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        if len(s1) > len(s2):
            return False


        window = Counter()
        c1 = Counter(s1)

        l = 0
        for i, ch in enumerate(s2):
            window[ch] += 1

            if i >= len(s1): #Update the left character  and deletiting as necessary
                leftChar = s2[i-len(s1)]
                window[leftChar] -= 1
                if window[leftChar] == 0:
                    del window[leftChar]

            if window == c1: return True
        
        return False


