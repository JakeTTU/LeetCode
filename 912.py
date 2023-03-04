'''
https://leetcode.com/problems/sort-an-array/
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid
            left_temp, right_temp = [None] * (n1), [None] * (n2)

            for i in range(n1):
                left_temp[i] = arr[left + i]
         
            for j in range(n2):
                right_temp[j] = arr[mid + 1 + j]
                
            i,j,k = 0,0,left
            while i < n1 and j < n2:
                if left_temp[i] <= right_temp[j]:
                    arr[k] = left_temp[i]
                    i += 1
                else:
                    arr[k] = right_temp[j]
                    j += 1
                k += 1
                
            while i < n1:
                arr[k] = left_temp[i]
                i += 1
                k += 1
                
            while j < n2:
                arr[k] = right_temp[j]
                j += 1
                k += 1
                
        def mergeSort(arr, left, right):
            if left < right:
                mid = left+(right-left)//2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid+1, right)
                merge(arr, left, mid, right)
            return arr
