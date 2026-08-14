class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       # we can super brute force it by checking each cell and dfs'ing through it, but we can also
       # track a "visited" list (since we only have to check each piece of land once overall)
       # for outer loop, go until we find a 1 that is not in visited, then go into it:
       # Then we dfs up down left right, adding to our total for each piece of land we find, and then
       # returning that value at the end
       # then just track the overall max value as we check each 1 in our outer loop
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # set of tuples (row, col)
        curr_area = 0
        max_area = 0

        def dfs(row: int, col: int) -> None:
            nonlocal curr_area

            # base cases (either out of bounds or water or visited)
            if (
                row < 0 or row >= ROWS or col < 0 or col >= COLS 
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return
            
            # else, we have land!, so inc our counter, and dfs all directions
            curr_area += 1
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # outer loop
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_area = 0
                    dfs(row, col)
                    max_area = max(max_area, curr_area)
        return max_area

        # visited={(0, 1)}
        # curr=18
        # max=0

            
