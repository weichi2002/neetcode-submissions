class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        c1 = Counter(s1)
        window = Counter()

        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            if (r-l+1) == len(s1): #if our current window equals 
                if c1 == window:
                    return True
                else:
                    window[s2[l]]-=1
                    if window[s2[l]] == 0:
                        del window[s2[l]]
                    l+=1

        return False

        #cap
        #papc


        