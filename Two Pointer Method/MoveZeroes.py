#Problem Link
#https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        l = 0 # left pointer 
        for r in range(len(nums)): # right pointer
            if nums[r]: # check if value that right ptr is on is non zero
                nums[l], nums[r] = nums[r], nums[l]  #swap
                l += 1
        return nums