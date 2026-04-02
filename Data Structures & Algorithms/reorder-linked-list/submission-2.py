# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Understand:
        Reorder list by pointing each node to its corresponding 
        node at the end of the list.


        Method:

        Plan:
        Split list using slow and fast pointer and dummy node
        Reverse second list
        Merge the two splits alternatively

        Implement:
        '''
        slow, fast = head, head.next

        # Split list
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse 2nd list
        second = slow.next
        prev = slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        # Merge alternatively
        first, second = head, prev
        while second:
            l1, l2 = first.next, second.next
            first.next = second
            second.next = l1
            first = l1
            second = l2
