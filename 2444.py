'''
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
'''

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        outsideIndex = -1
        minIndex = -1
        maxIndex = -1
        result = 0

        for i, n in enumerate(nums):
            if not minK<=n<=maxK:
                outsideIndex = i
            if minK == n:
                minIndex = i
            if maxK == n:
                maxIndex = i
            
            begIndex = min(minIndex, maxIndex)
            if begIndex > outsideIndex:
                result += begIndex - outsideIndex
                
        return result
