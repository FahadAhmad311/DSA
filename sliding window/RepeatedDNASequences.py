#additional question
#problem link 
#https://leetcode.com/problems/repeated-dna-sequences/

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen, res = set(), set()
        for l in range(len(s) - 9):
            cur = s[l:l + 10] # take index starting from l to l + 10(non inclusive)
            if cur in seen:
                #if this window in in seen hashset add it to res hashset
                res.add(cur)
            #if this window hasnt been seen before add it to seen hashset now
            seen.add(cur)
        #return the list of res windows
        return list(res)
        