class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force this: start with k = 1, check the hours, if > h, increment k and continue
        # O(n * m) where n is the length of piles and m is the resulting k

        # the absolute maximum k within the time frame is the max value of the array (since its h value
        # would be == len(piles))
        # the absolute minimum k is 1
        # trying to find some value in between this search space that fits our constraints
        # looking like a binary search! if k is too small, just search right,  if k is too large / 
        # it is valid, then seasrch left to find a possibly better solution
        # basically binary searching for the first True to appear in the search space
        # must keep track of smallest valid k, complete binary search, then return that
        # [F F F F T T T]

        l, r = 1, max(piles)
        min_valid_k = float("inf")

        while l <= r:
            k = (r + l) // 2

            # calculate num of hrs to eat all piles with this k value
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            
            # binary search condition
            if hrs > h:
                # search right (invalid, so must increase k)
                l = k + 1
            else:
                # if valid, then search left to potentially find a smaller k
                max_valid_k = min(min_valid_k, k)
                r = k - 1
        return max_valid_k

        # piles = [1,4,3,2], h = 9
        # l = 2 | r = 1
        # k = 1