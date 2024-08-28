#problem Link
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution(object):
    def twoSum(self, numbers, target):
        l , r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return[1 + l, 1 + r]