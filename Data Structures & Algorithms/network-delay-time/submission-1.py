class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this is just a djikstra's problem, where we want to go through all of the graph, getting the min path
        # to each node, then we want to return the largest value of our path (that we actually used)
        # we can use a minheap to track our current nodes, where we track (path, node) and minimize the path to choose
        # the next node to operate on.

        # first, build the adj list
        adj = {x : [] for x in range(1, n + 1)}
        for time in times:
            adj[time[0]].append([time[1], time[2]])
        
        heap = [[0, k]]
        visited = set()
        while heap:
            path, node = heapq.heappop(heap)
            if node in visited:
                continue
            # push all neighbors into the heap
            for nei in adj[node]:
                if nei[0] not in visited:
                    heapq.heappush(heap, [path + nei[1], nei[0]])
            visited.add(node)
            if len(visited) == n:
                return path
        return -1


