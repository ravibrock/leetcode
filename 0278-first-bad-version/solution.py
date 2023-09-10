# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        floor, ceiling = 1, n
        while floor <= ceiling:
            temp = int((ceiling + floor) / 2)
            if isBadVersion(temp) and isBadVersion(temp - 1): ceiling = temp - 1
            elif not isBadVersion(temp) and not isBadVersion(temp - 1): floor = temp + 1
            else: return temp
