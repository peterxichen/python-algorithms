# Reorder List (return L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …)
# 3 problems: find middle (2 pointer, one slow one fast) ->
# reverse list -> merge list
# time: O(N), space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # find middle of linked list
        p1 = p2 = head # p1 slow, p2 fast
        while p2 and p2.next:
            p1 = p1.next # p1 stops at middle
            p2 = p2.next.next
        
        # reverse second part of list (in place)
        prev, this = None, p1
        while this:
            this.next, prev, this = prev, this, this.next

        # merge two sorted linked lists
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next
        