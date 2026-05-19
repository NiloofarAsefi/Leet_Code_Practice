# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_So_far):
            if not root:
                return 0
      
            left = dfs(root.left, max(root.val, max_So_far))
            right = dfs(root.right, max(root.val, max_So_far))
            ans= left + right 
            if root.val >= max_So_far:
                ans +=1
            return ans
        return dfs(root, float("-inf"))

                
                
            
        