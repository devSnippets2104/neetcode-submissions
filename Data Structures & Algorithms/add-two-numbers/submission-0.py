# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode(0)
        current=dummy
        p1,p2=l1,l2
        carry=0

        while p1 is not None or p2 is not None or carry !=0:
            num1=p1.val if p1 is not None else 0
            num2= p2.val if p2 is not None else 0
            total = num1 + num2 + carry
            digit= total % 10
            carry= total //10
            new_node=ListNode(digit)
            current.next=new_node
            current=current.next

            if p1 is not None:
                p1=p1.next
            if p2 is not None:
                p2=p2.next
        return dummy.next
        

        
        