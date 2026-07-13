class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute force, calc the dist for all the points (O(n)), then sort by min distance O(nlogn)
        # use a minheap -> sorts the list from min -> max by inserting into it by log(n), but for
        # each point, the total time complexity is still O(nlogn)
        # instead of sorting, convert it INTO a minheap (O(n)), then pop it k times, O(n + klogn)
        
        # first we loop through the points, and calculate the distances to go with them
        dists = []
        res = []
        for i in range(len(points)):
            dist = points[i][0] ** 2 + points[i][1] ** 2
            dists.append([dist, points[i]])
        
        # now heapify, and then pop the first k values to get the result
        heapq.heapify(dists)

        for _ in range(k):
            # only get the point
            point = heapq.heappop(dists)[1]
            res.append(point)
        return res