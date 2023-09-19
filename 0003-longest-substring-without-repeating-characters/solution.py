class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0, 1]: return len(s)

        j, m = 0, 0
        for i in range(1, len(s) + 1):
            count, dist = len(Counter(s[j:i])), len(s[j:i])
            if count != dist: j += 1
            else: m = max(dist, m)
        
        return m
