class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive binary decision tree, where at each step, we have a pointer
        # to the next number in nums, and we either append that number, or 
        # don't append that number for each number, then once we get to the end
        # we return our final list for that path
        # we can track our res list outside of the stack, and just pop from it
        # after we call down if adding 
        res = []
        subset = []
        def dfs(index: int) -> None:
            print("curr subset", subset, index)
            # base case
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # recursive step
            # incl current num
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            # !incl current num
            dfs(index + 1)
        dfs(0)
        return res