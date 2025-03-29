#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) #Linked list tạm để lưu kết quả, giá trị sẽ từ dummy.next 
        l3_current = dummy #Node kết quả hiện tại đang tham chiếu
        carry = 0
        while l1 or l2 or carry != 0:
            intermediate_sum = ((l1.val if l1 else 0) + (l2.val if l2 else 0)) + carry
            new_val = intermediate_sum % 10
            carry = intermediate_sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3_current.next = ListNode(new_val)
            l3_current = l3_current.next
        return dummy.next

