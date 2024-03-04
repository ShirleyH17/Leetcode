# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.runtimes = 0
        self.output = 0


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        
        self.inorderTraverse(root, k)
        return self.output
        
        

    def inorderTraverse(self, node, k):
        if not node:
            return None
        
        if node.left:
            self.inorderTraverse(node.left, k)
        self.runtimes += 1
        if self.runtimes == k:
            self.output = node.val
            return
        if node.right:
            self.inorderTraverse(node.right, k)