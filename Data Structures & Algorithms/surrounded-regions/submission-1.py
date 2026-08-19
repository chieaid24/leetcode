class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # brute force: starting from each cell out the outer perimeter
        # DFS/BFS through all the connnected ones, marking them as "safe"
        # then once we have gone all the way around, go through the board once
        # and mark all "non-safe" cells as X's
        # O(m*n)

        # could also just loop through all of the O's on the board, and check
        # if they are surrounded (if never see an edge, then return "isSurrounded=True"
        # and if not, return False
        # Also in the loop as we are going up the stack, if isSurrounded=True
        # we can then set the current cell = X, removing the repeated work, since
        # we are already "there" for each of the O's in that DFS thing
        # O(m*n), but better since there is NO repeated work -> lets do this one
        # This won't work! We have to remember the form of a DFS logic graph, where one
        # leaf can't effect another leaf in this design, for example if one leaf already
        # returned up as "surrounded" then another leaf is then searched and it returns "not"
        # surrounded, then we can't go back down the leaf and rechange it, ie we MUST do it
        # in 2 passes, so let's do the first design

        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int):
            # mark it (visited on dequeue)
            board[r][c] = "V"
            # now dfs through all of the of its neighbors
            if 0 <= r + 1 < ROWS and board[r + 1][c] == "O":
                dfs(r + 1, c)
            if 0 <= r - 1 < ROWS and board[r - 1][c] == "O":
                dfs(r - 1, c)
            if 0 <= c + 1 < COLS and board[r][c + 1] == "O":
                dfs(r, c + 1)
            if 0 <= c - 1 < COLS and board[r][c - 1] == "O":
                dfs(r, c - 1)

        # now for the first pass, let's dfs through all of the edges
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        
        # now that we've marked all of the non-surrounded O's as V's, lets replace those "V's"
        # with O's and O's with X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "V":
                    board[r][c] = "O"
