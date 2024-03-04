# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution(object):
    def __init__(self):
        self.node1, self.node2 = None, None


    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp = TreeNode(val)
        if not root:
            return temp
        
        self.findNode(root, val)
        
        # If both node1 and node2 exist
        if self.node1 and self.node2:
            if self.node1.right == self.node2:
                temp.right = self.node2
                self.node1.right = temp
            elif self.node1.right == None:
                self.node1.right = temp
            else:
                if self.node2.left == None:
                    self.node2.left = temp
        
        # If only node1 exist
        if self.node1 and not self.node2:
            self.node1.right = temp
        
        # If only node2 exist
        if not self.node1 and self.node2:
            self.node2.left = temp

        return root


    def findNode(self, root, val):
        if not root:
            return None

        if root.val < val:
            if not self.node1 or self.node1.val < root.val:
                self.node1 = root
            self.findNode(root.right, val)
        if root.val > val:
            if not self.node2 or self.node2.val > root.val:
                self.node2 = root
            self.findNode(root.left, val)

# Solution 2
# class Solution(object):
#     def insertIntoBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if not root:
#             return TreeNode(val)
        
#         if root.val < val:
#             root.right = self.insertIntoBST(root.right, val)
#         if root.val > val:
#             root.left = self.insertIntoBST(root.left, val)
#         return root