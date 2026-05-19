# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # we need a tree traversal method.
        # we want to traverse from root to leaves of the tree.
        # DFS is an optimal solution, time complexiy of O(d), d is depth of the tree
        # space complexity O(d), this is because dfs has a heap for the recursion.
        def dfs(root, path_value_so_far):
            # stopping condition,
            if not root:
                return False
            
            # if root is a leaf.
            if not root.left and not root.right:
                return path_value_so_far + root.val == targetSum
                # path_value_so_far += root.val
                # if path_value_so_far == targetSum:
                #     return True
                # else:
                #     False   
            path_value_so_far += root.val
            left_output = dfs(root.left, path_value_so_far) # node 4 returns True
            # for node 7 left_output = False
            right_output = dfs(root.right, path_value_so_far) # node 8 returns False
            # for node 2 right_output = True
            # for node 11, left_output = False and right_output = True
            return left_output or right_output
        return dfs(root, 0)     



        