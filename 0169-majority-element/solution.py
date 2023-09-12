class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n, x, y = Counter(nums), 0, 0
        for i, j in n.items():
            if j > x: x, y = j, i

        return y
