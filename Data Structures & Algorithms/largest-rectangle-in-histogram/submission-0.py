class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Notice that at each point we can compare it to its next values to see how long it can 
        # "stretch" to the left
        # if it ever encounters a value less than itself, then it terminates, and its max area is
        # (endIndex - startIndex) * height. This means that we pop it from consideration
        # once this condition is true, meaning our stack becomes an increasing stack, strictly increasing
        # as each value hasn't been "bounded" yet
        # At each point, we look at the stack and pop all of the elements that are taller than it
        # to keep it increasing, and doing so, calculate the max heights that each of those elements
        # got to. additioanlly, since when we pop, this value is smaller than the last, so we can stretch
        # the current index to start at the last element that we popped (extending to the left)
        # Then at the end, we'll have the stack of all the elements that are "unbounded" which we than
        # loop through and calculate their heights, with the end index being len(heights)
        # tools: breaking down intot smaller problems, by looking at each index at a time
        # deciding to go forward through the heights (doesn't matter in this case)
        # Finding the relationship with what we want to calculate (area) with how we can possibly
        # iterate (linearly by indexes) to understand how we can get this (endIndex - startIndex * height)
        stack = [] # need to track the index and height of each entry
        max_area = 0

        for i in range(len(heights)):
            # compare to front of stack, only after then push to stack
            start_index = i
            while stack and heights[i] < stack[-1][1]:
                old_index, old_height = stack.pop()
                # now that we popped, calculate its max area
                max_area = max(max_area, (i - old_index) * old_height)
                start_index = old_index
            stack.append([start_index, heights[i]])
        
        # now loop through the rest of the stack, and calculate final max_areas
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, (len(heights) - index) * height)
            
        return max_area
