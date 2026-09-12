class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # traverse once through the wordList creating a graph, where words that are diff by 1 letter are connected
        # by an edge, we can do this by having a map of our "patterns" where we track the 
        # pattern that each word may fall into, for example hit -> *it, where lit should also be added to this list
        # then when we check each word, we check each of it's pattern, and add it to that list. When doing our BFS (used
        # to find the shortest path) we do the same by checking each of the patterns to get our list of neighbors
        # then if endWord not in wordList, return, else DFS / BFS from our endWord to our beginWord

        # base case
        if endWord not in wordList:
            return 0

        # make our adj list
        patterns: defaultdict[str, list[str]] = defaultdict(list) # pattern to list of words associated with that pattern

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)
        
        # now our bfs to find the shortest path, let's use iterative BFS
        visited = set()
        path_len = 1
        Q = deque([beginWord])
        visited.add(beginWord)

        while Q:
            for _ in range(len(Q)):
                word = Q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in patterns[pattern]:
                        if nei == endWord:
                            return path_len + 1
                        if nei != word and nei not in visited:
                            # append to Q
                            Q.append(nei)
                            visited.add(nei)
            path_len += 1
        return 0






