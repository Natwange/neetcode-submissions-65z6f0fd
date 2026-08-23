# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        U: inorder traversal of nodes 
            I: tree
            O: list of tree node values
            C: iterative
            E: [] -> []
               [5] -> [5]

        M: Recursive DFS

        P: 
        # Base case
        if not node:
            return

        left = dfs(root.left.left)
        append root.left.left.val to list
        append root.left.val to list
        right = dfs(root.left.right)
        append root.left.right.val to list
            
        list = [root.left, root, root.right]

        left = dfs(root.left)
        res.append(left)
        res.append(root)
        right = dfs(root.right)
        res.append(right)
        
        '''
        res = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)               
            dfs(root.right)     

        dfs(root)
        return res



        