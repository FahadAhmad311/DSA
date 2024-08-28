#problem Link
#https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        #sorting algorithms -> merge sort, quick sort(nlogn) , bubble sort(O(n^2)), insertion sort 
        return sorted(s) == sorted(t) 