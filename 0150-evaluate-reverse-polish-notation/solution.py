class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+' : lambda b, a : a + b,
            '-' : lambda b, a : a - b,
            '*' : lambda b, a : a * b,
            '/' : lambda b, a : math.trunc(a / b)
        }

        stack = []
        for t in tokens:
            if t in ops.keys(): stack.append(ops[t](stack.pop(), stack.pop()))
            else: stack.append(int(t))
        
        return stack[0]
