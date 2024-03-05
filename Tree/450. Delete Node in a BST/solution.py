# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
# class Solution(object):
#     def __init__(self):
#         self.head = None


#     def deleteNode(self, root, key):
#         """
#         :type root: TreeNode
#         :type key: int
#         :rtype: TreeNode
#         """
#         self.storeRoot = root
#         return self.deleteNodeHelper(root, key)


#     def deleteNodeHelper(self, root, key):
#         if not root:
#             return self.storeRoot
        
#         if root.val == key:
#             # node doesn't have left or right
#             if not root.left and not root.right:
#                 if not self.head:
#                     return None
#                 if self.head.left == root:
#                     self.head.left = None
#                 else:
#                     self.head.right = None
#             # node doesn't have head but have left or right
#             elif not self.head:
#                 if not root.right:
#                     return root.left
#                 if not root.left:
#                     return root.right
#                 return self.insertNode(root.left, root.right)
#             # node has head, has left or (and) right
#             elif not root.right:
#                 if self.head.left == root:
#                     self.head.left = root.left
#                 else:
#                     temp = root.left
#                     self.head.right = None
#                     self.insertNode(self.head, temp)
#             elif not root.left:
#                 if self.head.right == root:
#                     self.head.right = root.right
#                 else:
#                     temp = root.right
#                     self.head.left = None
#                     self.insertNode(self.head, temp)
#             else:
#                 temp1 = root.left
#                 temp2 = root.right
#                 if self.head.left == root:
#                     self.head.left = None
#                 else:
#                     self.head.right = None
#                 self.insertNode(self.head, temp1)
#                 self.insertNode(self.head, temp2)
#             return self.storeRoot
#         else:
#             self.head = root
#             if root.val < key:
#                 return self.deleteNodeHelper(root.right, key)
#             if root.val > key:
#                 return self.deleteNodeHelper(root.left, key)
        
    
#     def insertNode(self, root, node):
#         if not root:
#             return node
        
#         if root.val < node.val:
#             root.right = self.insertNode(root.right, node)
#         if root.val > node.val:
#             root.left = self.insertNode(root.left, node)
#         return root

# Solution 2
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val == key:
            # if root has no left or right child node
            if not root.left and not root.right:
                return None
            # if root only has only one child node
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # if root has both left and right child nodes
            else:
                minNode = self.getMin(root.right)
                root.right = self.deleteNode(root.right, minNode.val)
                minNode.left = root.left
                minNode.right = root.right
                root = minNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root


    def getMin(self, root):
        if root.left != None:
            while root.left:
                root = root.left
        return root