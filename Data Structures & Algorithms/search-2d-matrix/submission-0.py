class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # at first glance seems like binary search
        # we can create "flatten" logic by using (row# * len(row[0])) + col to get out flattened
        # value, then we can run binary search on this, and to convert back we have
        # (flattened // len(rows[0])) -> rows, flattened % len(rows[0])-> cols
        NUM_ROWS, NUM_COLS = len(matrix), len(matrix[0])
        l, r = 0, (NUM_ROWS * NUM_COLS) - 1

        while l <= r:
            m = (r + l) // 2
            cell = matrix[m // NUM_COLS][m % NUM_COLS]
            if cell > target:
                # search left
                r = m - 1
            elif cell < target:
                # search right
                l = m + 1
            else:
                # found it!
                return True
        return False

        # l = 4
        # r = 4
        # m = 4
        # cell = 8
