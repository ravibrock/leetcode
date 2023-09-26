class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        s = [l for l in reversed(s)]
        signs = ["-", "+"]
        digits = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        def trim(s, char):
            while s:
                l = s.pop()
                if l != char: return s + [l]
        
        def clamp(num):
            if num > 2 ** 31 - 1: return 2 ** 31 - 1
            if num < 2 ** 31 * -1: return 2 ** 31 * -1
            return num

        # Trims whitespace
        s = trim(s, " ")
        if not s: return 0
        
        # Determines sign
        sign = 1
        if s[-1] == "-" or s[-1] == "+":
            l = s.pop()
            sign = -1 if l == "-" else 1
        
        # Trims leading zeroes
        s = trim(s, "0")
        if not s: return 0

        # Stops if whitespace is found
        s2 = []
        while s:
            l = s.pop()
            if l not in digits.keys(): break
            s2.append(l)
        
        # Calculates integer:
        if len(s2) == 0: return 0
        power, total = 0, 0
        while s2:
            l = s2.pop()
            total += digits[l] * 10 ** power
            power += 1

        return clamp(total * sign)
