class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # since we want to remove duplicates, what we can do is sort the 
        # array (O(nlogn) < O(2^n) since at each decision it is a binary
        # decision, whether to include that number or not
        # but when we sort it, and we can avoid duplicates by when we "don't include"
        # a number, we skip ALL of the instances of that number.
        # This avoids the possibility that we create duplicate instances, like
        # [1, 2] [2, 1] (since skipping the "first" one will skip ALL of the ones)
        # Additionally, since we want to deal with solutions that have multiple
        # of the same number, when we "keep" a number, we just pass the next index
        # in, regardless of whether it is the same or not (to allow for cases like
        # [1, 1]. Classing DFS / backtracking, but with just sorting
        nums.sort()
        res = []
        subset = []

        def dfs(index: int) -> None:
            # base case
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # our two cases: 1st, we add it
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            # we ignore it (and all of its duplicates)
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1)
        dfs(0)
        return res
        # sub=[]
        # [1, 1, 2]
        # res=[[1,1,2] [1, 1] [1] [2] [] ]

