class Solution:
    def isValid(self, s: str) -> bool:
        pairs, stack = {"(": ")", "[": "]", "{": "}"}, []

        for l in s:
            if l in pairs.keys(): stack.append(l)
            elif l in pairs.values():
                if len(stack) == 0 or l != pairs[stack.pop()]: return False
        
        return len(stack) == 0
