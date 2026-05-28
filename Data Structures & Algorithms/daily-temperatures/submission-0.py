class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force solution: for every entry, loop through the array again to find the
        # next warmer day (O(n^2))

        # better solution (slightly better to keep track of possible greater or less
        # temperatures in an increasing stack) only slightly more efficient than just checking
        # the next largest temperature - store the value, index pair
        # at any point we have to pop from the stack, we should update the res array, at the index
        # we just popped from and with the difference between that index and the one we just found
        # that is greater
        
        res = [0] * len(temperatures)
        stack = [] #contains [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # pop from stack & update res array
                popped_index = stack.pop()[1]
                res[popped_index] = i - popped_index
            stack.append([t, i])
        
        # for each temp left in the stack (unfound), we set their index = 0
        while stack:
            popped_index = stack.pop()[1]
            res[popped_index] = 0
        return res