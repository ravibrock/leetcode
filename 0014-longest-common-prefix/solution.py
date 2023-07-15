class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        prefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            prefix += strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != strs [0][i]:
                    return prefix[0:i]
        return prefix
