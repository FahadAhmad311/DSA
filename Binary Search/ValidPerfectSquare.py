#problem Link
#https://leetcode.com/problems/valid-perfect-square/description/

class Solution(object):
    def isPerfectSquare(self, num):
        l, r = 1, num
        while l <= r:
            mid = (l  + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False # if value not found 