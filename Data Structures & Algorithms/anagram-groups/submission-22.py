class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #On2

        #we should be using a dictionary to sort to sort this
        groups = defaultdict(list)

        #using bucket method

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] += 1
            groups[tuple(freq)].append(s) #cast it into tuple to be able to be hashable
        
        return list(groups.values())