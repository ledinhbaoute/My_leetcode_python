#https://leetcode.com/problems/remove-element/
class Solution1:
    #Không tối ưu do việc xóa phần tử phải thực hiện dịch phần tử của mảng sang trái
    def removeElement(self, nums: List[int], val: int) -> int:
        k, i = len(nums), 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                k-=1
            else:
                i+=1
        return k

class Solution2:
    #Tối ưu bằng cách dùng k để giữ vị trí của phần tử không bằng val
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k