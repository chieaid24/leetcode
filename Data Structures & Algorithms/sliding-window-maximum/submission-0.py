class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force, create hte sliding window of size k every time, then search through it and find the maximum
        # need some sort of sorted list by maximums that you can check for every step
        # we can get this by using a decreasing deque!
        # where at each point, in the deque we store the index of the largest value up until this point
        # this reduces the repeated work of checking whether some values are larger than others -> we just have to keep
        # the largest one, and as backups, we append the smaller ones after that (hence only decreasing)
        # So at each point that we evaluate, check if it is larger than the right-most value in Q
        # if so, then pop that value, and continue until not true
        # This allows us to position the next "max value" as the window slides
        # as once the left bound of the window crosses the left-most element in the deque (curr largest
        # element) then we know to pop it, and now our next "max value" is in the correct position
        # it is also important to store the index in our queue rather than just the value for this
        # purpose -> so we know whether to pop from the left or not
        max_int_in_windows = []
        queue = collections.deque()
        l, r = 0, 0
        while r < len(nums):
            # check if we have to pop right
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            # check if we have to pop left
            if l > queue[0]:
                queue.popleft()
            
            # append to res, only if window is large enough
            if (r - l) + 1 == k:
                max_int_in_windows.append(nums[queue[0]])
                l += 1
            r += 1
        return max_int_in_windows