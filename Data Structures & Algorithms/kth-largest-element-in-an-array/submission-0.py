class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force: sort it decreasing, get the k-1th index (o(nlogn))
        # also could make a maxheap, and pop from it k times O(n) + o(klogn)
        # we can make a maxheap by negating all values pushed to our heapq minheap
        # (there is a heapify_max in new pythons, but just to practice, we'll negate all our values)
        heap = [-x for x in nums]
        heapq.heapify(heap)

        # pop from it k times, return the kth value
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

