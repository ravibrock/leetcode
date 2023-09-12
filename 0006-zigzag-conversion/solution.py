class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < 2: return s

        n, ss = 0, ["" for _ in range(numRows)]

        while n < len(s):
            if n % (numRows - 1) == 0:
                for j in range(numRows):
                    if n < len(s):
                        ss[j] += s[n]
                        n += 1
            else:
                ss[numRows - 1 - (n % (numRows - 1))] += s[n]
                n += 1
        
        return "".join(ss)
