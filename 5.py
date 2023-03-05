'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        maxP = ''
        l = len(s)
        flag = False
        for i in range(1,l):
            beg = i-1
            end = i+1

            if len([*set(s[beg:end+1])]) > math.ceil(len(s[beg:end+1])/2):
                continue

            while beg >= 0 and end <= l:
                if s[beg:end] == s[beg:end][::-1] and len(s[beg:end]) > len(maxP):
                    maxP = s[beg:end]
                    flag = True
                    
                if s[beg:end+1] == s[beg:end+1][::-1] and len(s[beg:end+1]) > len(maxP):
                    maxP = s[beg:end+1]
                    flag = True
                
                if not(s[beg:end] == s[beg:end][::-1] or s[beg:end+1] == s[beg:end+1][::-1]):
                    break
                
                beg -= 1
                end += 1

        return maxP if flag else s[0]
