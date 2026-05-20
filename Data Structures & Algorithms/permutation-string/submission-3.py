class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force: check every substring, and check if it is a permuatation using a dictionary / sorting it -> O(n^2 * n)
        # better solution: first store the ref_letters in s1 in a dictionary (we can make it an array if needed to save space)
        # then we can use sliding window technique in the s2, such that if the letter is not in our dict, then we inc both
        # and if it is, then we inc r pointer


        # better solution, realize that the permutation MUST be the same length as s1, thus we can have a fix window
        # of size len(s1) and then slide it, so we only go through n times
        
        # quickly code that up
        # make our s1 into a hashmap
        target_letters = [0] * 26
        for l in s1:
            target_letters[ord(l) - ord('a')] += 1
        
        max_window_size = len(s1)
        l, r = 0, 0
        window_letters = [0] * 26
        while r < len(s2):
            window_letters[ord(s2[r]) - ord('a')] += 1
            if (r - l) + 1 == max_window_size:
                # check equality, if so return true, if not, continue on and clear the window
                if tuple(target_letters) == tuple(window_letters):
                    return True
                else:
                    # increment l, reset r
                    window_letters[ord(s2[l]) - ord('a')] -= 1
                    l += 1

            r += 1
        return False




            

