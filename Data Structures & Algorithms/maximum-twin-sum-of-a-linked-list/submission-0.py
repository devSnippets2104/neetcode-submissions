# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        current=head

        while current:
            arr.append(current.val)
            current=current.next
        
        res=0
        i,j=0,len(arr)-1

        while i <j:
            res=max(res,arr[i]+arr[j])
            i+=1
            j-=1
        return res
        