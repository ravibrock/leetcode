import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).lower().replace("_", "")
        
        if len(s) == 0:
            return True

        for i in range(int(len(s) / 2)):
            if s[i] != s[-(i + 1)]: return False
        
        return True
