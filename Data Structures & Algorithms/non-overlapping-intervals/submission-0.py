class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # we can do this by first sorting the array -> this allows us to 
        # traverse left to right and easily see whether adjacent pairs
        # are overlappping
        # when comparing the two adj pairs there are two cases:
        # overlapping: 2nd start is < 1st end
        #   In this case we want to take the interval that ends earlier, and delete the other (greedy)
        # non-overlapping: do nothing, just move onto looking at the next interval
        rmv_count = 0
        # sort them first
        intervals.sort(key = lambda x : x[0])
        # get the currend, and loop until the end of the array
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # check if overlapping the last interval
            if start < last_end:
                rmv_count += 1
                last_end = min(last_end, end)
            else:
                last_end = end
        return rmv_count

        # count = 1
        # last_end = 4
        # [[1,2],[1,4],[2,4]]
