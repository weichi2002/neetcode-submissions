class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for item in strs:
            s += str(len(item)) + "#" + item
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        
        return ans