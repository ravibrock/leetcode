class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cur = 0
        length = len(nums) - 1

        while cur <= length:
            m = int((length + cur) / 2)
            if nums[m] < target: cur = m + 1
            elif nums[m] > target: length = m - 1 
            else: return m
            
        return -1
