#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
class Solution2:
    #Dùng hash table để giảm độ phức tạp
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        #Tạo một dict với các cặp key-value là giá trị và chỉ số của phần tử trong mảng
        for i in range(len(nums)):
            numMap[nums[i]]=i
        # Tính giá trị của target trừ cho từng phần tử, nếu có tồn tại trong dict và value của phần tử đó khác 
        # chỉ số phần tử hiện tại thì trả về cặp giá trị đó
        for i in range(len(nums)):
            if target - nums[i] in numMap.keys() and numMap[target - nums[i]] != i:
                return [numMap[target - nums[i]], i]