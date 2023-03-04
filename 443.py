'''
https://leetcode.com/problems/string-compression/
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        start = chars[0]
        s = [chars[0]]
        count = 1
        for i in chars[1:]:
            if i == start:
                count += 1
            else:
                start = i
                if count != 1: s.append(str(count))
                count = 1
                s.append(i)
        if count != 1:
            s.append(str(count))
            
        s = [*(("").join(s))]

        for i in range(len(s)):
            chars[i] = s[i]
            
        while len(s) < len(chars):
            chars.pop()
        
        return(len(chars))
