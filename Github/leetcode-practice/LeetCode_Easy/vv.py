# class TreeBui:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxdepth(self, root: Optional[TreeBui]) -> int:
#         if not root:
#             return 0
        
#         left= self.maxdepth(root.left)
#         right = self.maxdepth(root.right)
#         return max(left, right)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # True or False return 
        def dfs(root, curr):
            if not root:
                return False
            
            if root.left ==None and root.right== None:
                return curr + root == targetSum
            
            else:
                curr += root.val 

            left_val = dfs(root.left, curr)
            right_val = dfs(root.right, curr)

            return left_val or right_val
        return dfs(root, 0)


            
            

