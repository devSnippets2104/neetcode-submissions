class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def get_length(self):
        current=self.head
        length=0

        while current is not None:
            length+=1
            current=current.next
        return length
    
    def get(self, index: int) -> int:
        current=self.head
        count=0
        while current is not None:
            if count == index:
                return current.val
            count+=1
            current=current.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        length=self.get_length()
        if index < 0 or index > length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == length:
            self.addAtTail(val)
            return
        new_node=Node(val)
        current=self.head
        for _ in range(index - 1):
            current=current.next
        new_node.next=current.next
        current.next=new_node
        

    def deleteAtIndex(self, index: int) -> None:
        length=self.get_length()
        if index < 0 or index >= length:
            return
        if index == 0:
            self.head=self.head.next
        else:
            current=self.head
            for _ in range(index - 1):
                current=current.next
            current.next=current.next.next