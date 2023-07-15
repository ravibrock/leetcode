class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
        needle = hash(needle)
        for i in range(h - n + 1):
            if hash(haystack[i:i+n]) == needle:
                return i
        return -1
