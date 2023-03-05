'''
https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0 #Left staring index
        r = len(height)-1 #Right Starting index
        maxA = ((r) - l) * min(height[r], height[l]) #init maxA as area of widest rect

        while l < r: # as long as the rect has width
            if height[l] > height[r]: # move index of side with the shorter height
                r-=1
            else:
                l+=1
            if ((r) - l) * min(height[r], height[l]) > maxA: # check area of new rect
                maxA = ((r) - l) * min(height[r], height[l]) # update maxA if new max

        return maxA 
