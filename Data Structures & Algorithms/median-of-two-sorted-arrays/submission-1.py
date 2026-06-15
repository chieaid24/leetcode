class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         # brute force: append lists into 1 large list, then find median of that list (O(n))
         # basis of this is that when finding a median, we have to find a left partition and a right
         # partition such that it upholds an overall sorted array
         # We know what the partition size must be (total_len // 2), so therefore
         # we can manipulate one of the arrays to search through it and try to find the partition point
         # where the other array's partition is half - partition_1.
         # Then, our condition we are looking for is that is the next value from the first partition
         # less than the next value from the second partition and vice versa? Since this will mean that 
         # our left partition is correct (all values are smaller than all values in the right partition)
         # at this point, we can stop searching and return either the next min value (odd) or the 
         # average between the two values (even)
        combined = len(nums1) + len(nums2)
        half = combined // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # run binary search through nums1
        l, r = 0, len(nums1) - 1
        # to be able to correctly get the ends -> nums1 partition could be nothing, or be all
        # we have to set the start value to -inf and end value to +inf to show this relationship
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            # now, calculate the partitions for boths nums1 and nums2, setting equal to +-inf if OOB
            # (values, since we are comparing them later)
            nums1_left = nums1[m1] if m1 >= 0 else float("-inf")
            nums1_right = nums1[m1 + 1] if m1 + 1 < len(nums1) else float("inf")
            nums2_left = nums2[m2] if m2 >= 0 else float("-inf")
            nums2_right = nums2[m2 + 1] if m2 + 1 < len(nums2) else float("inf")

            # run our condition, such that the left partition must be strictly less than the right partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # good condition, we return this (with logic to check whether even or odd)
                if combined % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return min(nums1_right, nums2_right)
            elif nums1_left > nums2_right:
                # shift left
                r = m1 - 1
            else:
                l = m1 + 1


        # nums1 = [1, 2]
        # nums2 = [3]

