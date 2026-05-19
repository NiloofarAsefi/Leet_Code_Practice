# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
#         if not root:
#             return 0
        
#         if root.left == None:
#             return self.minDepth(root.right) + 1
#         elif root.right == None:
#             return self.minDepth(root.left) + 1
#         else:
#             return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        if not root:
            return 0
        left= self.minDepth(root.left)
        right= self.minDepth(root.right)
        
        if left==0:
            return right +1
        elif right ==0:
            return left +1
        else:
            return min(left, right)+1
        
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.left.left = None
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# minDepth(root)