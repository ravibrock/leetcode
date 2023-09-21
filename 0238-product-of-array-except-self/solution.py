class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre, post = [1] * length, [1] * length

        for i in range(1, length):
            pre[i] = nums[i - 1] * pre[i - 1]
            post[length - i - 1] = nums[length - i] * post[length - i]

        return [pre[i] * post[i] for i in range(len(pre))]
