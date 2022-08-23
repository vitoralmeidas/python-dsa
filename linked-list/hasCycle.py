# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers
# both start in the head, but faster will 'walking through' 2 times more faster than slower
# if bot

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slower = head
        faster = head

        while (slower and faster):
            faster = head.next.next
            slower = head.next

            if(slower == faster):
                return True
        return False
