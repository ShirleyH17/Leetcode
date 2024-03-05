# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N) time complexity solution
# class Solution(object):
#     def __init__(self):
#         self.sum = 0

#     def countNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return self.sum
        
#         q = deque([root])
#         while q:
#             self.sum += len(q)
#             for i in range(len(q)):
#                 cur = q.popleft()
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
        
#         return self.sum

# Optimal solution
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        hl, hr = 0, 0
        l, r = root, root
        while l:
            hl += 1
            l = l.left
        while r:
            hr += 1
            r = r.right
        if hl == hr:
            return 2 ** (hl) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)