class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)
        #use the sorted key as the and append to each list, and gather from the hashmap together

        for s in strs:
            sortedS = "".join(sorted(s))
            hashMap[sortedS].append(s)
        
        res = []
        for val in hashMap.values():
            res.append(val)
        
        return res
        
        
    
