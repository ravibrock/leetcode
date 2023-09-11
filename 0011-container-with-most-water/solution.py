class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        def calcvol(): return (r - l) * min(height[l], height[r])
        vol = calcvol()

        while l != r:
            if height[l] < height[r]: l += 1
            else: r -= 1
            vol = max(vol, calcvol())
        
        return vol
