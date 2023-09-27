class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        while len(longest) < len(s):
            for n in range(len(s) // 2):
                if s[:n+1] == s[n+2:2*(n+1)+1][::-1]:
                    if 2 * (n + 1) + 1 > len(longest): longest = s[:2*(n+1)+1]
                elif s[:n+1] == s[n+1:2*(n+1)][::-1]:
                    if 2 * (n + 1) > len(longest): longest = s[:2*(n+1)]
            s = s[1:]
        
        return longest
