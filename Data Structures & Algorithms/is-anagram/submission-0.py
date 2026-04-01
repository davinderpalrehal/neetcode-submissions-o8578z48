class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for a, b in zip(s, t):
            s_count[a] += 1
            t_count[b] += 1
        
        for k in s_count.keys():
            if s_count[k] != t_count[k]:
                return False
        
        return True