class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # brute force: 
        # track the # of opens that we have currently in our string
        # if its 0, then we must open (or end the string)
        # if its > 0, then we have 2 choices: either close it (then decrement the cnt)
        # or open another one (if we have opens remaining)
        # then we just continue until we've gone through all possibilites
        # time complexity: O(n (copy) * 2^(2n) <- since for every n ther are
        # 2 characters) space: O(n (copy) * 2^(2n) recursion) (O(N) auxilliary)
        res = []
        path = []

        def dfs(opened: int, closed: int) -> None:
            # base case
            if opened == 0:
                if closed == n:
                    # append to res
                    res.append("".join(path))
                    return
                path.append("(")
                dfs(opened + 1, closed)
                path.pop()
            else:
                # 2 routes, open another (if poss) and close it, then continue
                if opened + closed < n:
                    path.append("(")
                    dfs(opened + 1, closed)
                    path.pop()
                # close it
                path.append(")")
                dfs(opened - 1, closed + 1)
                path.pop()
        
        dfs(0, 0)
        return res
        # n = 3
        # o=2, c=0
        # path = [( ( ) ]
        # res [((()))]

                