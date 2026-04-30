class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to use a hashmap to store strings the with the same count
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
            


        