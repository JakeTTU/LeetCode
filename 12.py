'''
https://leetcode.com/problems/integer-to-roman/
'''

class Solution:
    def intToRoman(self, num: int) -> str:

        romans = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 
                    'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000} # roman Numeral info

        s = '' #init return string

        for i in list(romans.items())[::-1]: #iterrate over roman characters largest to smallest
            t = num//i[1] * i[0] #calc valid number of chars to append for curr value 
            s = s + t #add roman character to string
            num = num % i[1] #subtract converted value from input number

        return s
