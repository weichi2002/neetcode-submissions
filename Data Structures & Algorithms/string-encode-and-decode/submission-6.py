class Solution:

    #add some sort of delimite
    #how do we know when to stop?
    #we need to know the length of the string

    #how can we know the end of the length?
    #the input might be a string
    #we can add a manual delimiter at the end to tell us we reached the end of string and we should extract the length
    #use the length to cut out the array from the stirng
    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "$" + st
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            #extract the length
            while s[r] != "$":
                r+=1
            length = int(s[l:r])
            l = r+1
            r = l + length
            res.append(s[l:r])
            l = r


        return res
