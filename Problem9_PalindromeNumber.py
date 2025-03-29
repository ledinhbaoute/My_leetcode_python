#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]]=i
        for i in range(len(nums)):
            if target - nums[i] in numMap.keys() and numMap[target - nums[i]] != i:
                return [numMap[target - nums[i]], i]