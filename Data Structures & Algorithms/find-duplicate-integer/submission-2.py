class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # smarter way to do this:
        # notice that since each integer in within the range [1, n], we can map each value onto 
        # an INDEX! as a pointer. ie a value of 1, is a pointer to index 1. 
        # now that we have that, we realize that repeated values, all point to the same index (we need
        # to find said index) to do this, we can use a cycle detection algorithm, since that index
        # that multiple indexes point to, is the start of a cycle! (draw it out)
        # How do we detect where a cycle starts in a linkedlist -> floyd's algorithm, and to do this
        # we do normal fast + slow ptrs to find intersection (cycle exists) then we start another slow
        # pointer at the beginning of our list (in this case index 0) and when they meet, that is the
        # start of our cycle
        slow, fast = nums[0], nums[nums[0]]
        # find intersection point
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # at intersection pt, start our second slow ptr
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow
        
