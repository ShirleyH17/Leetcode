# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution(object):
    def __init__(self):
        self.temp = -sys.maxint
        self.valid = True


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorderTraverse(root)
        return self.valid
        

    def inorderTraverse(self, root):
        if not root:
            return None
        
        if root.left:
            self.inorderTraverse(root.left)
        if root.val <= self.temp:
            self.valid = False
            return
        self.temp = root.val
        if root.right:
            self.inorderTraverse(root.right)

# Solution 2
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         def isValidBSTHelper(root, min_node, max_node):
#             if not root:
#                 return True
            
#             if min_node and root.val <= min_node.val:
#                 return False
#             if max_node and root.val >= max_node.val:
#                 return False
#             return (isValidBSTHelper(root.left, min_node, root) and isValidBSTHelper(root.right, root, max_node))
        
#         return isValidBSTHelper(root, None, None)