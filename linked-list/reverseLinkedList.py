# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        if head == None:
            return []

        prev, curr = None, head
        nxt = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
