# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
U: reordering the linked list alternatively
    I: linked list
    O: reordered linked list
    C:
    E: [1,2,3,4] -> [1,4,2,3]
        [1,2,3] -> [1,3,2]
        [2] -> [2]

M: [2,4,6,8,10]      [2,4,6,8]
        s                 s
             f                 f
    [2,4,6]    [10,8]       [2,4,6] [8]
    [2,4] [8,6]              

P: 
if only 1 node, return head
split the list using slow and fast
reverse second list
link nodes alternatively
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        '''
        M: [2,4,6,8,10]      [2,4,6,8]
                s                 s
                     f                 f         
        [2,4,6]    [10,8]       [2,4,6] [8]
        [2,4] [8,6]

        [8,10]   
        '''

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        prev = None
        while second:
            nxt = second.next  #nxt = 10
            second.next = prev  # scd.nxt=none
            prev = second
            second = nxt
          #         sp     
        #[2,4,6]    [<-8<-10]
        #     cf
        # 2->10->4->8->6
        curr = head
        while prev:
            first = curr.next
            curr.next = prev
            sec = prev.next
            prev.next = first
            prev = sec
            curr = first


            

        




        