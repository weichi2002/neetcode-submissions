class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "$" + s
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            
            #we found the separtator and we can extract number
            length = int(s[i:j])
            i = j+1 #skip the separator
            j = i + length
            string = s[i:j]
            res.append(string)
            i = j #update the i to keep the while loop going


            #do logic 
        return res

