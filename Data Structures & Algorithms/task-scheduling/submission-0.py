class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # brute force: create a dict of all letters + their occurences
        # then an outer while loop loops until dict is empty, inner for loop loops over each
        # KV in the dict once, keeping track of the current "n" then (n+1 for each loop), after exiting, append extra cycles as
        # needed, then go until completely empty
        # tc: o(N + N) sc: O(N)

        # but additionally, we need to consider that we ALWAYS want to evaluate the char with teh max
        # occurences first (to get its cooldown going), and we can store ongoing max occurences with 
        # a maxheap! additionally, we can also use a Q to store the values that are on their cooldown
        # and we can store it with their (val, time) where time is the time that they can be added back
        # into our heap, then we just continue until our maxheap is empty. Our heap should only store
        # occurences, doesn't matter the character
        char_to_occ = defaultdict(int)
        for task in tasks:
            char_to_occ[task] += 1
        occ = list(char_to_occ.values())
        heap = [-x for x in occ]
        heapq.heapify(heap)
        Q, time = deque(), 0
        print(heap)

        while heap or Q:
            time += 1
            # first check the Q to see if we can pop any values, and add them to the heap
            if heap:
                # now evaluate the top of the heap
                val = heapq.heappop(heap)
                val += 1
                if val != 0:
                    # add to Q
                    Q.append((val, time + n))
            if Q and Q[0][1] <= time:
                heapq.heappush(heap, Q.popleft()[0])

        return time


