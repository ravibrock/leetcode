class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        s = ""
        combs = [s + l for l in letters[digits[0]]]

        if len(digits) > 1:
            for digit in digits[1:]:
                chars = letters[digit] * len(combs)
                combs = [combs[n] for n in range(len(combs)) for _ in range(len(letters[digit]))]
                for n in range(len(chars)): combs[n] += chars[n]
        
        return combs
