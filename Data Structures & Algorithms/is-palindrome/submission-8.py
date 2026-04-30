class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1

        while p1 < p2:
            while not s[p1].isalnum() and p1 < len(s)-1:
                p1 += 1
            while not s[p2].isalnum() and p2 > -1:
                p2 -=1
            
            if s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1

            else:
                return False
        
        return True


    
