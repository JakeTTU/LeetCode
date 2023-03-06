'''
https://leetcode.com/problems/can-convert-string-in-k-moves/
Time: O(N)
'''

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        #return false if strings are not same length
        if len(s) != len(t): return False
        char_change = [-1] * 27 #init record list
        
        for a,b in zip(s,t): #iterrate over both strings at same time
            
            #diff = number of chars s[i] is away from t[i]
            diff = (ord(b) - ord(a)) %26
            
            char_change[diff] += 1 #record change at diff index

        # check if number of encoutered shifts // 26 is greater than k-i
        # only check if there was a shift ignoring index 0 in char_change list
        return(all([char_change[i] <= (k - i) // 26 for i in range(1, 27)])) 
