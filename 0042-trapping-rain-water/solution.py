class Solution:
    def trap(self, height: List[int]) -> int:
        formax, backmax = [height[0]], [height[-1]]
        for i in range(1, len(height)):
            formax.append(formax[i - 1] if formax[i - 1] > height[i] else height[i])
            backmax.append(backmax[i - 1] if backmax[i - 1] > height[-(i + 1)] else height[-(i + 1)])
        backmax = list(reversed(backmax))

        solution = []
        for i in range(1, len(height) - 1):
            gap = min(formax[i - 1], backmax[i + 1]) - height[i]
            solution.append(gap if gap > 0 else 0)
        
        return sum(solution)
