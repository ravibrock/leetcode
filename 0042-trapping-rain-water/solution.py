class Solution:
    def trap(self, height: List[int]) -> int:
        formax, backmax = height.copy(), height.copy()
        for i in range(1, len(height)):
            formax[i] = formax[i - 1] if formax[i - 1] > height[i] else height[i]
            backmax[-(i + 1)] = backmax[-i] if backmax[-i] > height[-(i + 1)] else height[-(i + 1)]

        solution = []
        for i in range(1, len(height) - 1):
            gap = min(formax[i - 1], backmax[i + 1]) - height[i]
            solution.append(gap if gap > 0 else 0)
        
        return sum(solution)
