'''
https://leetcode.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s = s[1:] + s[:1]
        s = s[::-1]
        if abs(int(s)) < 2**31:
            return int(s)
        else:
            return 0
