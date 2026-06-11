# ideally, you want a list with the main key sorted by time, to easily find the "next valid time"
# we could do this by repeatedly calling .sort() for every set (no bc that would be o(nlogn) every time)
# where we can also just iterate through the list to see where to place it and it would be o(n)
# we could also use binary search to find the next valid place which would be o(logn)\
# then similarly, to to find the next key, we can use binary search as well
# however, we also should sort by the key, so the general structure should be
# dict: {key, [(time, value), (time, value)]}
# with this, looking up the correct "stream" is o(1), then inserting the correct time, value pair 
# is O(logn)

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) # {key : [(time, value), (time, value)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # insert at end of list (always in increasing order)
        self.time_map[key].append((timestamp, value))
        print(self.time_map)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map.keys():
            # search the list, find @ the value, or right below it
            l, r = 0, len(self.time_map[key]) - 1
            closest_value = ""
            while l <= r:
                m = (l + r) // 2
                curr_time = self.time_map[key][m][0]
                if curr_time > timestamp:
                    # search left
                    r = m - 1
                elif curr_time < timestamp:
                    # search right (and this is a possible solution)
                    closest_value = self.time_map[key][m][1]
                    l = m + 1
                else:
                    return self.time_map[key][m][1]
            return closest_value
        else:
            return ""