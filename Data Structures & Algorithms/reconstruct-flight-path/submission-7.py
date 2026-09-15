class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        tickets.sort(reverse=True)

        for src, dst in tickets:
            adj.setdefault(src, []).append(dst)

        res = []

        def dfs(src):
            while src in adj and adj[src]:
                dst = adj[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")
        return res[::-1]