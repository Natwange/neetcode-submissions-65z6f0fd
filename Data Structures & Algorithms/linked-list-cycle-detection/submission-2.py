# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Understand:
        Looking for a cycle in the linked list
        Return true if cycle exists, otherwise false
        Cycle always starts from the tail node to the index-th
        index
        Edge cases:
        [] -> false
        [1,2], index 1 -> return True
        [1,2], index 1 -> return False

        Method: Slow pointer-fast pointer


        Plan:
        if 
        slow, fast = head, headnnext
        while fast
        slow, fast = slow.next, fast.next.next

        Implement:

        Review:

        Evaluate:
        '''
        if not head:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        
        return False


