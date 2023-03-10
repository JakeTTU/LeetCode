'''
https://leetcode.com/problems/add-two-numbers/
'''
class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        lt = ListNode()
        l3 = lt

        carry = 0
        while l1 and l2:
            sum = (l1.val+l2.val) % 10
            l3.val = (l1.val+l2.val+carry) %10
            carry = (l1.val+l2.val+carry) // 10
            if l1.next or l2.next or carry == 1:
                l3.next = ListNode(1)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        l = l1 if l1 else l2

        while l:
            l3.val = (l.val+carry) %10
            carry = (l.val+carry) // 10
            if l.next or carry == 1:
                l3.next = ListNode(carry)
            l = l.next
            l3 = l3.next

        return lt
 


    

        

