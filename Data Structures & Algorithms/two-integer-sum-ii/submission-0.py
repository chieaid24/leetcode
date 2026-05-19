class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers, since it is sorted, we can set our two pointers to the end, and use how our current sum compares
        # to our desired sum, and decrease (by dec right pointer) or increase (by inc left pointer) go until they cross
        # or we find the target
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        # numbers = [1,2,3,4], target = 3
        #            L   R