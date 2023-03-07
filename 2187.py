'''
https://leetcode.com/problems/minimum-time-to-complete-trips/
'''

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        # 0 < min_time < min(trip)*totalTrips
        l, r = 0, min(time) * totalTrips

        # binary search
        while l <= r:
            mid = (l + r)//2
            
            #check if total trips satisfied
            if sum([mid//x for x in time]) >= totalTrips:
                #set answer
                ans = mid
                
                #check remaining left half
                r = mid-1
            else:
                #check remaining right half
                l = mid+1
                
        return ans
