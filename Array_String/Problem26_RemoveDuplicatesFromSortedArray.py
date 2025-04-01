#https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        val=nums[0]
        for i in range(1, len(nums)):
            if val<nums[i]:
                nums[k] = nums[i]
                val = nums[i]
                k+=1
        return k