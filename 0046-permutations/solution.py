class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.recursive(nums)
        return self.perms

    def recursive(self, nums, cur=[]):
        if len(nums) > 0:
            for n in range(len(nums)):
                self.recursive(nums[:n] + nums[n + 1:], cur + [nums[n]])
        else:
            self.perms.append(cur)
