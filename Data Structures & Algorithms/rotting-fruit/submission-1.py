class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi node BFS, where each starting "rotting fruit" is a node we can search from, then
        # from these starting positions, we just do normal multinode BFS.
        # when we are searching through the array in the beginning to find the rotting fruit, lets
        # keep a counter of ALL the fruit, so we can compare it to our visited set, and see if we hit
        # all of the fruit through our traversal. Then we just go until our Q is empty
        ROWS, COLS = len(grid), len(grid[0])
        Q = deque()
        visited = set()

        total_fruit = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                total_fruit += 1
                if grid[row][col] == 2:
                    Q.append((row, col))
                    visited.add((row, col))
        if total_fruit == 0:
            return 0
        
        # now our main BFS loop
        minutes = -1
        while Q:
            # we need to loop layer by layer, since we are tracking the # of minutes
            for _ in range(len(Q)):
                r, c = Q.popleft()
                grid[r][c] = 2

                # go through its neighbors, if they are valid (==1, in bounds) then we add it to Q
                if 0 <= r + 1 < ROWS and (r + 1, c) not in visited and grid[r + 1][c] == 1:
                    Q.append((r + 1, c))
                    visited.add((r + 1, c))
                if 0 <= r - 1 < ROWS and (r - 1, c) not in visited and grid[r - 1][c] == 1:
                    Q.append((r - 1, c))
                    visited.add((r - 1, c))
                if 0 <= c + 1 < COLS and (r, c + 1) not in visited and grid[r][c + 1] == 1:
                    Q.append((r, c + 1))
                    visited.add((r, c + 1))
                if 0 <= c - 1 < COLS and (r, c - 1) not in visited and grid[r][c - 1] == 1:
                    Q.append((r, c - 1))
                    visited.add((r, c - 1))
            minutes += 1
        return minutes if len(visited) == total_fruit else -1
                    