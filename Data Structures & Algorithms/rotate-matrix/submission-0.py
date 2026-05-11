class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # looking at a diagram of this problem. we see that we can set the bounds of our
        # square (since we are only looking at the outer ring at a time) to be L, R, T, B
        # Then we can loop through it n - 1 times, where we can actually iterate through counterclockwise
        # (to save on temporary variables), swapping each in that certain position
        # then we iterate again with our pointer being the 2nd, going to the 2nd position on each
        # row / col
        # then we decrement the main L, R, T, B pointers, if they ever cross,  then we exit and return
        L, R, T, B = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while L < R:
            
            for i in range(R - L):
                # BL -> TL
                temp = matrix[T][L + i]
                matrix[T][L + i] = matrix[B - i][L]
                # BR -> BL
                matrix[B - i][L] = matrix[B][R - i]
                # TR -> BR
                matrix[B][R - i] = matrix[T + i][R]
                # TL -> TR
                matrix[T + i][R] = temp
            L += 1
            R -= 1
            T += 1
            B -= 1