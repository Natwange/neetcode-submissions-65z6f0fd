# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        E: if only one node -> false
            [1,2,3,4]
             s
              f
            s is head
            f is head
            while fast exists:
                move s 1-step and f 2-step
                if s equals f:
                    return true
                else: continue
            return False
        '''
        if not head:
            return False

        s, f = head, head.next
        # s = 1, f = 2
        if not f:
            return False

        while f and f.next:
            s = s.next  # s= 2
            f = f.next.next  #f= 

            if s == f:
                return True
            else:
                continue
        return False

