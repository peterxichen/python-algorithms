# Remove Nth Node from End of Linked List
# 1 pass, 2 pointers, one start at n+1, other from start
# time: O(num nodes), space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 pointers (one advances from n+1, other from start)
        first = second = dummy = ListNode(0)
        
        dummy.next = head # corner case: single node, delete head
        for i in range(n+1): # start at n+1
            first  = first.next
        
        while first: # second pointer ends at n-1
            first = first.next
            second = second.next
        second.next = second.next.next # "delete"
        return dummy.next
