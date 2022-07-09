# Detect Cycle in Linked List
# two pointer (fast & slow) will eventually meet w/ cycle
# OR created dict of "visited" nodes, space O(n)
# time: O(n), space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # if 1 behind, then will meet next iter
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next # increment by 1
            fast = fast.next.next # increment by 2
        return True
