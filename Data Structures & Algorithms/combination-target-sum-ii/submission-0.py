class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # when it says that we cannot have duplicate combinations, how can we
        # solve this? well, we can sort the array! This allows us to put the 
        # repeated numbers next to each other. In essence, we are trying
        # to only have each number (when we skip it) to skip it, AND its sibling
        # equal numbers (else, we will end up with duplicate pairs, like [2, 6] [6, 2])
        # So, when we do our "skip this number" step, instead of just incrementing
        # once, we should increment it until it is a unique number, so then the 
        # solutions down this branch do not collide with the solutions on the "keep" branch
        # however, in the "keep" case, we want to just continue normally (just inc by 1)
        # since in this keep case, we DO want to include repeat numbers, such as [2, 2, 4]
        candidates.sort()
        res = []
        path = []

        def dfs(index: int, sum: int) -> None:
            # base case
            if sum == target:
                # return this path
                res.append(path.copy())
            elif index >= len(candidates) or sum > target:
                return
            else:
                # first case: add to path
                path.append(candidates[index])
                dfs(index + 1, sum + candidates[index])
                path.pop()
                # second case: don't add this to the path, and the next should
                # be a unique number (we don't want ANY of this specific number
                # in the path going forward)
                while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                    index += 1
                dfs(index + 1, sum)
        dfs(0, 0)
        return res
        