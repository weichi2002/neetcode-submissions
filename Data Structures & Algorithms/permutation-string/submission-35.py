class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        freq1 = [0] * 26
        freq2 = [0] * 26

        for s in s1:
            freq1[ord(s)-ord('a')] += 1

        l = 0

        for r in range(len(s2)):
            freq2[ord(s2[r])-ord('a')] += 1
            if (r-l+1) == len(s1): 
                if freq1 == freq2:
                    return True
                freq2[ord(s2[l])-ord('a')] -=1
                l+=1
              
        return False

        #cap
        #papc


        