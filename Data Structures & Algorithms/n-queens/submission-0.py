class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
       # brute force:
       # if we think about doing brute force across each row (since we know that each row can only
       # hold a single queen, we can just go row by row)
       # now as we go down to the next row, how do we know if its valid or not? Well, it cannot be in 
       # the same column as any previous queen (so store a col set), and cannot be in the + diagonal (BL -> TR)
       # and cannot be in the - diagnoal (TL -> BR). But, how can we store these diagonals as in index?
       # Well, we remember that the - diagonal, each step, the row += 1 and col += 1, so therefore, row - col
       # is constant (our index). Similarly, in the + diagonal, for each step col += 1, row -= 1, so therefore
       # row + col is constant (use this as our index). Then we can have a brute force approach
       # where for each "level" of our tree we have n decisions (placing the queen in each of the cols for
       # that row) and we just check if its valid, if so place a queen there and continue, if not
       # then return
        res = [] # List[List[str]]
        path = [] # List[int] (will convert to string before appending to res to save on time complexity)

        cols = set()
        posDiag, negDiag = set(), set()

        def dfs(row: int) -> None:
            # base case:
            if row == n:
                board = [] # List[str]
                for col in path:
                    row_str = "." * col + "Q" + "." * (n - col - 1)
                    # row_str = row_str[:col] + "Q" + row_str[col + 1:]
                    board.append(row_str)
                res.append(board)
                return
            
            # recursive case, checking each of the cols
            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue
                # this is a valid place, so put a queen here, update the sets, and recurse
                path.append(col)
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                dfs(row + 1)
                path.pop()
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
        dfs(0)
        return res
        # n = 4
        # path=[]
        # cols=[], posD=[], negD=[] 