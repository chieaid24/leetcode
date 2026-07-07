# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal, left to right, for each level, return the value of the last
        # node hit for that level
        # for level order traversal, we use a Q, take the size of the Q, and iterate that amt of times
        # for each "level"
        # base case
        if not root:
            return []
        Q = deque()
        Q.append(root)
        res = []
        
        while Q:
            lvl = len(Q)
            last_val = None
            for i in range(lvl):
                node = Q.popleft()
                if not node:
                    continue
                Q.append(node.left)
                Q.append(node.right)
                last_val = node.val
            if last_val is not None:
                res.append(last_val)
        return res
        #res=[1, 3, 5]
        # last_val = 5
        # lvl = 4
        # [ N N N N ]

        