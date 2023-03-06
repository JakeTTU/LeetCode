'''
https://leetcode.com/problems/kth-missing-positive-number/
Binanry Search
Time O(logN) ; Space O(1)
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n, l = len(arr), 0 #init num of elements in arr & left pointer
        r, l2 = n-1, n #init right pointer & left boundry pointer

        while l <= r: 
            mid = l + (r - l)//2 #find midpoint index
            missing = arr[mid] - (mid +1) #find what midpoint should be and compare
            
            if missing < k: # search remaining right half if missing less than K
                l = mid + 1
            
            elif missing >= k: # search remaining left half if missing >= than K
                l2 = mid
                r = mid-1
                
        return(l2 + k) # at l2 k positive numbers missing (the kth missed number is lb + k)

'''
Time O(N) ; Space O(1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = 0
        m = k
        while n < len(arr) and arr[n] <= m:
            m += 1             
            n += 1
        return m

'''
