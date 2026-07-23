class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # brute force: convert nums -> set, then we have a "working set" for each
        # path that we go down, where for example if we choose 1 as the starting
        # int, our set will contain [2,3] where we want to return the permutations
        # of this set appended to our current permutation of [1]
        # at each loop, we for each loop through the working set, once there
        # is nothing in the working set, we append the current path to the res
        res = []
        path = []

        def dfs(num_set: List[int]) -> None:
            # base case
            if not num_set:
                res.append(path.copy())
                return
            
            # recursive step
            for i in range(len(num_set)):
                # take this element, make it our "first" and then pass the rest of 
                # the list into a child step (brute force it and create a new array
                # each time)
                path.append(num_set[i])
                dfs(num_set[:i] + num_set[i + 1:])
                path.pop()
        dfs(nums)
        return res
    # res=[[1,2,3] ]
    # path=[1,]
    # numset=[1,2,3]

