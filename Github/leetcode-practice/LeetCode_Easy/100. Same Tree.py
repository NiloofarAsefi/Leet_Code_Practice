# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # if both roots of p and q are null, return T, else, F
            if p == None and q == None:
                return True 
            elif p == None or q== None:
                return False 
            # first check the value of roots of p or q 
            if p.val != q.val:
                return False
         
            left= dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            # I also can say (return left and right)
            if left == False or right == False:
                return False
            else:
                return True
        return dfs(p, q)

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if p == None and q == None:
#             return True
        
#         if p == None or q == None:
#             return False
        
#         if p.val != q.val:
#             return False
        
#         left = self.isSameTree(p.left, q.left)
#         right = self.isSameTree(p.right, q.right)
#         return left and right

