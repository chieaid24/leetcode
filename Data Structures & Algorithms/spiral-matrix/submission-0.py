class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Brute force: 
        # recursive problem is "layers" from the outside
        # TL -> TR, TR -> BR, BR -> BL, BL -> TL
        # go to next layer (update the bounds for L, R, T, B)
        # Brute force is to just "hardcode" each the directions we must go then execute them in order
        #
        # we can slightly optimize this that at each time we complete a row / col, we can update our pointers
        # Then when we update, we can check if our pointers are crossing, if so then we exit
        res = []
        L, R = 0, len(matrix[0]) - 1
        T, B = 0, len(matrix) - 1
        
        while L <= R and T <= B:
            # first, we go TL -> TR
            for x in range(L, R + 1):
                res.append(matrix[T][x])
            # now update our pointer, now that we finished the top row
            T += 1
            if T > B:
                return res
            
            # now we go TR -> BR
            for y in range(T, B + 1):
                res.append(matrix[y][R])
            R -= 1
            if L > R:
                return res
            
            # now we go BR -> BL
            for x in range(R, L - 1, -1):
                res.append(matrix[B][x])
            B -= 1
            if T > B:
                return res
            
            # now we go BL -> TL
            for y in range(B, T - 1, -1):
                res.append(matrix[y][L])
            L += 1
            if L > R:
                return res
        return res
            
        # L, R = 0 0
        # T, B = 1 0