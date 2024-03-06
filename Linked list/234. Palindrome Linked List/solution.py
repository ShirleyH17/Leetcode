# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1 - use stack to compare
class Solution(object):
    def __init__(self):
        self.left = None
        self.right = None


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.left, self.right = head, head
        return self.traverse(self.right)


    def traverse(self, right):
        if not right:
            return True
        res = self.traverse(right.next)
        res = (res and (self.left.val == right.val))
        self.left = self.left.next
        return res


# Solution 2 - only reverse part of the linked list to compare
    
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Use fast and slow pointers to find the middle of the linked list
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = self.reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True

    
    def reverse(self, head):
        pre, cur, next = None, head, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre