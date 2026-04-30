class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #On2

        #we should be using a dictionary to sort to sort this
        groups = defaultdict(list)

        for s in strs:
            groups["".join(sorted(s))].append(s)
        
        return list(groups.values())