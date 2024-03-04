# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0


    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.right:
            self.convertBST(root.right)
        
        root.val += self.sum
        self.sum = root.val

        if root.left:
            self.convertBST(root.left)
        
        return root