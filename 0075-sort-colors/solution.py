class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for _ in range(len(nums)):
            for n in range(1, len(nums)):
                if nums[n] < nums[n - 1]:
                    temp = nums[n - 1]
                    nums[n - 1] = nums[n]
                    nums[n] = temp
