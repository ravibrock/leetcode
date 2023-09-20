class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i == 0: n, i = num, 1
            elif n == num: i += 1
            else: i -= 1
        
        return n
