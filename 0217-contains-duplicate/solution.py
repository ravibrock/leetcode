class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = Counter(nums)
        for i in test.values():
            if i > 1: return True
        return False
