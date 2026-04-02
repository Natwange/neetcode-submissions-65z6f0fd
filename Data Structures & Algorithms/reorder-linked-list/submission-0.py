# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Understand:
        Reorder a linked list to this order:
        n = len(linked_list)
        [0, n-1, 1, n-2, 2, n-3, 3, ...] these are indices

        Example:
        head = [2,4,6,8] -> [2, 8, 4, 6]
        head = [2,4,6,8,10] -> [2, 10, 4, 8, 6]

        Edge cases:
        Empty: head = null -> none
        Duplicates: head = [2,2,2,3,3] -> [2,3,2,3,2]
        Single node: head = [5] -> [5]
        Two node: head = [1,2] -> [1,2]

        Plan:
        1. Find middle element using slow/fast pointer
        2. Reverse second half list
        3. Merge the two lists alternatively

        Implement:
        '''
        slow, fast = head, head.next
        
        # Find middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second list
        second = slow.next
        prev = slow.next  = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2







