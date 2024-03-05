# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left >= right:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        # Go to one node before position left
        p01 = self.goPosition(dummy, left - 1)
        # Position left and its next node
        p1, p1n = p01.next, p01.next.next
        # Go to one node before position right
        p02 = self.goPosition(dummy, right - 1)
        # Position right and its next node
        p2, p2n = p02.next, p02.next.next
        
        if p1n == p2:
            p01.next = p2
            p2.next = p1
            p1.next = p2n
        elif p1n == p02:
            p01.next = p2
            p2.next = p1n
            p1n.next = p1
            p1.next = p2n
        else:
            p01.next = p2
            p2.next = p1n
            p02.next = p1
            p1.next = p2n
        
        head = dummy.next
        return self.reverseBetween(head, left+1, right-1)
    

    def goPosition(self, start, position):
        for i in range(position):
            start = start.next
        return start