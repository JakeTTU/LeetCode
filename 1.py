'''
https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check = {}
        i = 0
        while target - nums[i] not in check:
            check[nums[i]] = i
            i += 1
        return [check[target - nums[i]], i]

'''
## Better space complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                return [i,nums.index(target - nums[i])]
'''
