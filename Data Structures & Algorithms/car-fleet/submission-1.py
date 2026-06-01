class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # how can we brute force this? 
        # starting from the car in the front-most position, see the time it takes to get to 
        # target (in ex 1, 3), now going to the next position, check the time to get to target (3 as well)
        # if it takes LONGER than the next car, it becomes the next "blocker", and ++ a fleet
        # if it takes SHORTER or EQUAL to next car, then it gets combined with that car (take the max
        # between the times) as it has been blocked, and joined a fleet
        # This also requires that the position list be sorted descending
        # Time complexity -> O(nlogn + n)

        # better solution: we realize that the situation is a monotonically increasing stack, where 
        # every entry in the stack is another fleet (and the values in the stack are time to destination)
        #
        # times: [5 5 4 2]

        # code up the brute force
        # sort the positions and their related speeds
        # idea is to combine them into a list of tuples, then sort that?
        # or we can use the zip() function, which takes two lists, packs them into tuples,
        # then we sort that, then we unzip with zip(*zippped_list) and convert that to a list
        # in this case we don't even have to unzip, we can just leave it as a list of lists
        cars = list(sorted(zip(position, speed), reverse=True)) # [[position, speed], [position, speed]]
        fleets = 0
        limiting_time = 0

        for pos, sp in cars:
            # calc time to get to target
            time = (target - pos) / sp
            if time > limiting_time:
                fleets += 1
                limiting_time = time

        return fleets

        # fleet = 1
        # limit = 1
        # [8 7 6 5 4 3 ] 
