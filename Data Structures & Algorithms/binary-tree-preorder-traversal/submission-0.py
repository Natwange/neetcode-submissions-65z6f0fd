# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            #Base
            if not root:
                return

            res.append(root.val)  #res = [1,2,4,5,3,6,7]
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res
            



