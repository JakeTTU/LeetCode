'''
https://leetcode.com/problems/zigzag-conversion/
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = list(range(numRows))
        pattern = rows + list(range(numRows-2, 0, -1))
        cyles = math.ceil(len(s)/len(pattern))
        patterns = pattern*cyles

        new = [''] * numRows

        for i, char in zip(patterns, s):
            new[i] += char

        return "".join(new)
