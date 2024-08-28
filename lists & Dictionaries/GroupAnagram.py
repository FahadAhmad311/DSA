#Problem link
#https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26  # [0, 0, .... 0, ] 26 zeroes 
            for c in s:
                count[ord(c) - ord("a")] += 1
                # 97 - 97 -> 0 - a
                # 98 - 97 -> 1 - b
                # 99 - 97 -> 2 - c
            res[tuple(count)].append(s)
        return res.values() 
        