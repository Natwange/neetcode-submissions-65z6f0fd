# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        list_len = 0
        curr = head
        dummy = ListNode(0)
        dummy.next = head

        while curr:
            list_len += 1
            curr = curr.next

        curr = head
        target = list_len - n + 1
        if target == 1:
            dummy.next = curr.next
            return dummy.next

        count = 1
        while curr:
            if count == target - 1:
                curr.next = curr.next.next
                return dummy.next
            count += 1
            curr = curr.next






