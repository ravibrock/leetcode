class Solution(object):
    def twoSum(self, nums, target):
        max = len(nums)
        x = 0
        while x < max:
            i = nums[x]
            y = 0
            while y < max:
                if i + nums[y] == target:
                    if y != x:
                        return [x, y]
                y += 1
            x += 1
