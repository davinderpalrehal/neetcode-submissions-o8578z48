class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:
            pre = ''
            for i in range(len(s)):
                if i >= len(res):
                    break
                if s[i] != res[i]:
                    break
                pre += s[i]
            res = pre

        return res
