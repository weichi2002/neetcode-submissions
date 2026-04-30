class Solution:

    def encode(self, strs: List[str]) -> str:
        #we could use a delimiter, but the input could possible contian. We probably wnat to throw a unique identifer
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            word = s[i: j]
            res.append(word)

               
            i = j
        
        return res


            
            
            
            