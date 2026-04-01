class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for word in strs:
            curr = ''
            for i in range(min(len(res), len(word))):
                if res[i] != word[i]:
                    break
                curr += word[i]
            res = curr

        return res