# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if not fast or not fast.next:
                return False
            if slow == fast:
                return True
        
        return False