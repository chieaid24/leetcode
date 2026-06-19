class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force, keep a set, and if a new num is alr in set, return it
        # O(n) time, O(n) space -> can we solve in O(1) space?
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)