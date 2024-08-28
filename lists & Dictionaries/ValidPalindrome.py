#problem Link
# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        new = ''
        #alpha numeric characters -> commas and spaces nhi /n this 
        for c in s:
            if c.isalpha() or c.isdigit():  # either only alphabets or digits -> True or False 
                new += c.lower()        # -> all captial letters have to be changed into small letters
        return (new == new[::-1]) 