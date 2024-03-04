# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution(object):
    def __init__(self):
        self.output = None


    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.searchBSTHelper(root, val)
        return self.output
    
    
    def searchBSTHelper(self, root, val):
        if not root:
            return None 
        
        if root.val == val:
            self.output = root
            return
        elif root.val < val:
            self.searchBSTHelper(root.right, val)
        else:
            self.searchBSTHelper(root.left, val)
        
# Solution 2
# class Solution(object):
#     def searchBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if not root:
#             return None 
        
#         if root.val < val:
#             return self.searchBST(root.right, val)
#         elif root.val > val:
#             return self.searchBST(root.left, val)
#         else:
#             return root