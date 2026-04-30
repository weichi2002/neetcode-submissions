class Solution:

    #we just add a delimiter
    def encode(self, strs: List[str]) -> str:
        res = ""
        #add a delimiter
        #but thsi delimter might not be working
        #how do we know based on where to split
        #we want to add the length of each array before we add it
        for s in strs:
            res += str(len(s)) + "#" +  s
        return res
        
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res
        
        
        
        
