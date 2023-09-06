class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        
        if len(s) == 0:
            return True

        for i in range(int(len(s) / 2)):
            if s[i] != s[-(i + 1)]: return False
        
        return True
