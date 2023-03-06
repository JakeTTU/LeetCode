'''
https://leetcode.com/problems/climbing-stairs/
Time O(N)
'''
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1 #only one way to advance one step

        a,b = 1,2
    
        for i in range(1,n-1): # iterrate n-2 times range(2, n)
            #ways to clime n steps quals result at n-2 + result at n-1
            a,b = b, a+b 
            
        return b #return result at n step
