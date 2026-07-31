class Solution:

    def check_palindrome(self, start: int, end: int, word: str) -> bool:
        while start <= end:
            if word[start] == word[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
       # brute force:
       # we have two pointers (current substring window)
       # we have two options at each step: 
       # we can go to the next (if our curr substring is a pal), moving our
       # pointers to the next index
       # or we can continue, just moving our right pointer, to take more of the 
       # string into our window, in case it could be a longer palindrome 
       # if our indexes are at the end, so we just return w nothing
       # aabb
       # [a a bb] [a a b b] [aa b b] [aa bb]
        res = []
        pals = []

        def dfs(start: int, end: int) -> None:
            # base case:
            # if it is a pal, then we append it to our pals list, if it at the end
            # then we add the pal list to res
            if start == end or self.check_palindrome(start, end, s):
                pals.append(s[start : end + 1])
                # at end of word
                if end == len(s) - 1:
                    res.append(pals.copy())
                    pals.pop()
                    return
                dfs(end + 1, end + 1)
                pals.pop()
            
            # if not a pal (or just want to continue searching, we just incr
            # the end to take in the next value)
            if end == len(s) - 1:
                return

            dfs(start, end + 1)
        
        dfs(0, 0)
        return res
        # res=[[a a b]]
        # pals=[a]
        # s=0 , e=0
    
