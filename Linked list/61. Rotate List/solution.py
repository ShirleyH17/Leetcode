# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head

        # k could be larger than the length of the linked list
        count = 0
        p = dummy
        while p.next:
            p = p.next
            count += 1

        actualTimes = k % count
        p1, p2 = dummy, dummy
        
        for _ in range(count-actualTimes):
            p1 = p1.next
        
        p2 = p1
        for _ in range(actualTimes):
            p2 = p2.next
        
        p2.next = dummy.next
        dummy.next = p1.next
        p1.next = None

        return dummy.next
