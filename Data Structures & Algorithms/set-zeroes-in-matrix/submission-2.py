class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # brute force is just check every cell if it is a 0, if so then loop through its top, bottom, left, right boundaries
        # and set all of those elements as 0 as well -> problem is that now we will think those 0s we just set are "original"
        # 0s which they are not.
        # Could potentially solve this by going through all of the directions, then calling this method recusirvely
        # with the 4 quadrants this operation created -> also can't work since a 0 in one quadrant can affect the cells in another
        # However, this still could be okay since for each "quadrant" we are just using pointers, it is not a new array
        # so we can still affect all other cells in the matrix.
        # Doing this ensures that the created 0s won't be acted on.
        # additionally, to make the code simpler, when we set the 0s, we can just go horizontal + vertical, not RLTB
        # O( (N*M)^2 ) time complexity, O(1) space complexity
        # we can scan in a way such that we update our outer bounds every time we finish a row / col so there is no 
        # repeating work
        # basically, every row that we scan, we just update the T bound to make it easy -> same time complexity 
        # if on any row we find a 0, then we set all 0s and can break
        # However, this still leads to repeat 0s being acted on
        # How can we solve this? Well, let's introduce some memory to store whether or not each row / col contains a 0!
        # since if ANY of the cells within that row/col, it means that entire row/col should be set to 0
        # we can initially do this with an extra O(N) array and a O(m) array to store this 0'd out flag for each row / col.
        # In this way, we store if we have to, but don't change anything yet! This makes it so we can correctly find 
        # all the original 0s, and then we change everything at the end!
        # However, if we want to change space, we can use the first row, and first column as our storage for this (with an extra
        # variable for overlap in the TL cell)
        # This way, we loop through each cell once, and if it is a 0, then we set its row flag and its col flag to = 0.
        # After going through all the cells, we can now go through our storage arrays, and set rows/cols to be 0
        # The aha moment here is a Time / Space tradeoff, where firstly, if we want to reduce time complexity we can introduce
        # space complexity. Additionally, to reduce time complexity we can do multiple "shallow" passes rather than a single
        # "deep" pass through the array. Also, caching in general, where we can store our work in variables to reduce repeated
        # work.
        first_row = matrix[0][0] 
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # set its row + col flags to 0
                    matrix[0][j] = 0
                    if i == 0:
                        first_row = 0
                    else:
                        matrix[i][0] = 0
        
        
        # now we loop through our flag array, and set rows + cols to be 0 (after logic is done, we can update the array,
        # so our logic doesn't interfere with itself)
        # instead of doing this,
        # let's break it down by looping through all of the cells not in 1st col / 1st row
        # (as to not break our logic)
        # then at the end we can loop through our first col + first row to correctly set our vars 
        
        # first as to not disrupt our logic, we only want to change non-flag cells
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                # if its row OR its col flag is 0, then we can set this to be 0 as well
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # now go through the flags to correctly see if have to update this first row
        # we only have to check the 0,0 for the row, since that's where it would have updated if a 0 exists on the left col
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        # now go through the first_row flag  to see if have to set the first row to be 0 as well
        if first_row == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
            

