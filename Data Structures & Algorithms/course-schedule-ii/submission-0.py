class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first step is go through all the prereqs and make our adjancency graph (dict[course : prereqs]
        # Then, when traversing through them, just pick them at random, and go until our
        # graph's adj list is empty -> since doing each course can only unlock other courses
        # (won't lock others, so doesn't really matter the order overall, just complete the
        # prereqs before the course) for every "completed course" ie a course with no prereqs
        # we need to mark it completed somehow, so we don't complete it again if multiple
        # courses have the same prereq -> maybe delete it from the graph.? this may mess up
        # our outer loop, so maybe just put a placeholder value in the list to say "completed"
        
        # make our adj graph
        crs_to_prereq: dict[int, list[int]] = {}
        for i in range(numCourses):
            crs_to_prereq[i] = []
        for prereq in prerequisites:
            crs_to_prereq[prereq[0]].append(prereq[1])
        
        path: list[int] = []
        visited: set[int] = set()
        
        # optimization: delete the kv pair when visit it, instead of setting it to inf
        def dfs(course: int) -> bool:
            # base case
            if course in visited:
                return False
            if crs_to_prereq[course] and crs_to_prereq[course][0] == float("inf"):
                return True
            
            # has some remaining prereqs that we must complete before marking this complete
            visited.add(course)
            for prereq in crs_to_prereq[course]:
                # eval each prereq
                if not dfs(prereq):
                    return False
            visited.remove(course)
            crs_to_prereq[course] = [float("inf")]
            path.append(course)
            return True
        
        # outer loop
        for course in crs_to_prereq.keys():
            if not dfs(course):
                return []
        return path

        # crs_to={0:[inf], 1:[inf], 2:[]}
        # path=[0 1 2]
        # visit={}