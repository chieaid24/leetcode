"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # notice when we draw a picture, that we can see the # of meeting rooms required
        # at any point is = to the # of meetings started - # of meetings ended
        # This means, if we iterate through our points from left to right (not in pairs)
        # then we can find this kind of relationship
        # however, we still need to track whether each value is a start or end value
        # since it changes the behavior of our count -> a start means that another
        # meeting room is required (another overlap is happening), and a end means that
        # one less meeting room is required, since an overlapping meeting ended
        # then we take the max value this count has been 
        # So, a way we can solve this is using a separate start and end arrays, where
        # we can use two pointers to loop through each array at a time
        # addtitionally, one of the base cases for this is if the values are equal
        # (there is a meeting starting and ending at the same time) by our problem statement
        # this is not considered a conflict (ie the ending one ends before the start one starts)
        # so we can just defer to the end one, decrement the count, and move on (the start one
        # will be analyzed next)

        # first let's create our start[] and end[] arrays
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        # now we do two pointers to loop through our arrays (once we get to the end
        # of start, we can exit, since looping through ends will only dec count)
        # also a start must come before an end
        count = 0
        max_count = 0
        s, e = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                # meeting started
                count += 1
                max_count = max(max_count, count)
                s += 1
            else:
                # meeting ended
                count -= 1
                e += 1
        return max_count
            
        
            
                

        

        # starts = [0 5 15]
        # ends = [10 20 40]
