class Solution:
    def longestPalindrome(self, s: str) -> int:
        x, n, i = Counter(s), 0, 0
        
        for value in x.values():
            if value % 2 == 0:
                n += value
            elif value != 1:
                n += value - 1 
                i = 1
            else:
                i = 1
        
        return n + i
