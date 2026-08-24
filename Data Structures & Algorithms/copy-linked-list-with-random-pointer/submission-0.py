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
        
        found={}

        current=head

        while current is not None:
            found[current]=Node(current.val)
            current=current.next
        
        current=head
        while current is not None:
            found[current].next=found[current.next] if current.next is not None else None
            found[current].random=found[current.random] if current.random is not None else None
            current=current.next
        return found[head]

        