#Problem Link
#https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        maplist = defaultdict()
        counter = 0
        for num in nums:
            if num not in maplist:
                maplist[num] = 1
            else:
                counter += maplist[num]
                maplist[num] += 1
        return counter