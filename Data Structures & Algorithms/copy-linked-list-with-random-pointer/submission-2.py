"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        current=head

        while current is not None:
            copy_node=Node(current.val)
            copy_node.next=current.next
            current.next=copy_node
            current=copy_node.next
        
        current=head
        while current is not None:
            current.next.random=current.random.next if current.random is not None else None
            current=current.next.next

        p1,p2=head,head.next
        copy_node=head.next

        while p1 is not None:
            p1.next=p1.next.next
            if p1.next is not None:
                p2.next=p2.next.next
            p1=p1.next
            p2=p2.next if p2 else None
        
        return copy_node

            
