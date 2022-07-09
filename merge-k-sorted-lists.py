# Merge K Sorted Lists
# helper method to merge 2 sorted lists
# divide and conquer merge k/2 each time
# time: O(nlogk) N nodes, k linked lists, space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge 2 sorted linked lists
        def merge(list1, list2):
            # recursive
            if list1 is None:
                return list2
            elif list2 is None:
                return list1
            elif list1.val < list2.val:
                list1.next = merge(list1.next, list2)
                return list1
            else:
                list2.next = merge(list1, list2.next)
                return list2
        
        if len(lists) == 0:
            return None
        
        # merge into k/2 lists each time (divide & conquer)
        # e.g. [0,1,2,3,4,5] -> [0,2,4] -> [0,4] -> [0]
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = merge(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]
