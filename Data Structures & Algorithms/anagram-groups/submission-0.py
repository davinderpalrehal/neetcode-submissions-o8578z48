class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)

        for word in strs:
            count = Counter(word)
            key = ''
            for k in sorted(count.keys()):
                key += k + str(count[k])
            groups[key].append(word)


        
        for key in groups.keys():
            res.append(groups[key])

        return res