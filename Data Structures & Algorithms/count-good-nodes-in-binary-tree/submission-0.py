# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # first pass: 
        # recursive DFS where we pass the max of that path downwards, if the current node's value
        # is greater than that, then return 1 + left + right, else return 0 if null / less than (but
        # continue until all nodes are traversed)
        # O(n) time, O(n) space, because you are recursing through each level
        def dfs(node: TreeNode, max: int) -> int:
            # base case
            if not node:
                return 0
            
            # recursive step
            if node.val < max:
                return dfs(node.left, max) + dfs(node.right, max)
            
            max = node.val
            return 1 + dfs(node.left, max) + dfs(node.right, max)
            
        # call our function
        return dfs(root, float("-inf"))

        # [3 3 N 4 2]