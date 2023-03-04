'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Written to find all starting indexes instead of only first. 

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indexes = []
        count = 0
        while needle in haystack:
            indexes.append(haystack.index(needle)+ count*len(needle))
            count += 1
            haystack = haystack.replace(needle,'',1)
        
        if indexes:
            return indexes[0]
        else:
            return -1
