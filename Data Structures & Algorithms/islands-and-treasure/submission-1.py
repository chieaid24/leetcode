class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # brute force, start from each land cell and BFS until it finds a treasure chest, then set that
        # value as its value
        # better: start at the treasure chests, BFS outward filling in all of the land (set it to the min
        # between its curr value and the curr distance) then repeat for all chests
        # BUT! this creates repeated work, so what we can do is actually do a multisource BFS, where we
        # are BFSing from all of the gates at once, ie doing it by layer so all of the land that is 
        # evaluated is confirmed to be the closest to that gate (so no repeat work)
        # track a Q, and a visited set, then we populate the Q with all the gates in the grid
        ROWS, COLS = len(grid), len(grid[0])
        Q = deque() # tracks (row, col)
        visited = set() # tracks (row, col)
        dist = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    Q.append((r,c))
        
        while Q:
            # loop through it on LEVELS at a time
            for _ in range(len(Q)):
                row, col = Q.popleft()
                if (row, col) in visited or grid[row][col] == -1:
                    visited.add((row, col))
                    continue
                visited.add((row, col))

                grid[row][col] = dist
                # call BFS on all valid neighbors
                if row + 1 < ROWS and (row + 1, col) not in visited:
                    Q.append((row + 1, col))
                if row - 1 >= 0  and (row - 1, col) not in visited:
                    Q.append((row - 1, col))
                if col + 1 < COLS and (row, col + 1) not in visited:
                    Q.append((row, col + 1))
                if col - 1 >= 0 and (row, col - 1) not in visited:
                    Q.append((row, col - 1))
            dist += 1