def convert(l):
    if l == "I":
        return 1
    if l == "V":
        return 5
    if l == "X":
        return 10
    if l == "L":
        return 50
    if l == "C":
        return 100
    if l == "D":
        return 500
    if l == "M":
        return 1000

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        s = list(map(convert, list(s))) + [0]
        while i < len(s) - 1:
            if s[i] < s[i + 1]:
                total += s[i + 1] - s[i]
                i += 1
            else:
                total += s[i]
            i += 1

        return total
