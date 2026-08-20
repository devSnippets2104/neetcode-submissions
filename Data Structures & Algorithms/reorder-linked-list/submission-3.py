# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getMiddle_ptr(self,head:Optional[ListNode]):
        slow=fast=head
        prev=None

        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        return prev,slow
    
    def reverse(self,start_node:Optional[ListNode]):
        prev=None
        current=start_node

        while current is not None:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        prev,mid=self.getMiddle_ptr(head)
        prev.next=None

        second_head=self.reverse(mid)

        p1=head
        p2=second_head

        while p1 is not None and p2 is not None:
            p1_next=p1.next
            p2_next=p2.next

            p1.next=p2

            if p1_next is not None:
                p2.next=p1_next
            
            p1=p1_next
            p2=p2_next

        