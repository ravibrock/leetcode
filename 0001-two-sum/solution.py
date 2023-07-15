class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for s in range(i+1, n):
                if nums[i] + nums[s] == target:
                    return [i, s]
