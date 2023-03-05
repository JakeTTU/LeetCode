'''
https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1: # return element if only in list
            return strs[0]

        pref = ''

        for i in range(min([len(x) for x in strs])+1): # check range of elements in shortest string
            p = strs[0][:i] # prefix of first element
            if all(s[:i] == p for s in strs): # if all elements share prefix, set prefix
                pref = p
            else:
                break # break if all prefixes dont match

        return pref
