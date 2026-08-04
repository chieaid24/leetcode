class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       # brute force:
       # dfs approach, where for each digit in our string, we loop through all of the possible
       # chars it could be, call them recursively, and then return (store the index at which we 
       # are looking) O(n * 4^n) (for each level, it is O(n) to create the new string, time complexity, where n is the length of digits

       # any way to improve the time complexity?
       # instead of recalculating all the way down for each letter, if we precompute the possibilities
       # at "one level down" it will the same possibilities no matter what letter we choose at this step
       # (and we just prepend this letter in front of all of thos possibilities)
       # [dg dh di eg eh ei fg fh fi] -> pass it up
       # [tdg tdh tdi teg teh tei tfg tfh tfi udg udh ...] -> pass it up
       #  In this way, we don't have to completely recompute, but instead, we just use a simple
       # for loop, also O(4^n)

       # solve it using the simple brute force!
        res = []
        dig_to_char = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        path = []

        def dfs(index: int) -> None:
            # base case
            if index == len(digits):
                if path:
                    res.append("".join(path))
                return
            
            # recursive
            for char in dig_to_char[digits[index]]:
                path.append(char)
                dfs(index + 1)
                path.pop()
        dfs(0)
        return res
        # 34
        # path=[d]
        # res=[dg dh]
