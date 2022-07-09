# Reverse Linked List
# single pass, two pointer (curr + prev)
# time: O(n), space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        this = head
        while this:
            temp = this.next
            this.next= prev
            prev = this
            this = temp
        return prev
