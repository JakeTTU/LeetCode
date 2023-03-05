'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        index, maxL = 0, 0
        
        for i,v in enumerate(s):
            if v not in d.keys():
                d[v] = []
            d[v].append(i)
            
            if v not in s[index:i]:
                if len(s[index:i+1]) > maxL:
                    maxL = len(s[index:i+1])
            else:
                index = d[v][len(d[v])-2]+1
        
        return maxL
