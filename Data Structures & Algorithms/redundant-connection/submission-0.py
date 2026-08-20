class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # brute force: recreate the graph rep. not including each edge, check if its still
        # connected and acyclical, then go through all of the edges, and return the last
        # valid edge
        # also optimization is loop through checking each edge backwards, so we can
        # just return the FIRST valid edge

        # we can also do Union Find! (Disjoint set) where we track the parents of each
        # node (with path compression) and the size of each group (since size will kind of
        # get messed up with the path compression)
        # Then we implement 2 functions: find(n) which returns the representative / root
        # of the group (with path compression to optimize it as we search)
        # and union(n1, n2) which merges two groups together, making the smaller group
        # (smaller size) the child of the larger group (bigger size) then we add the sizes
        # together to get the new size of the parent
        # now to solve this problem, we are trying to find the LAST edge that makes up a
        # loop (since only 1 loop, and we are looking for the last one) so therefore
        # the first time that the roots of the two nodes are equal (ie they are already
        # connected in some way -> so therefore this connection if we were to make it
        # would create a loop)
        num_nodes = len(edges)
        par = [i for i in range(num_nodes + 1)]
        size = [1] * (num_nodes + 1)
        
        def find(n: int) -> int:
            # returns the root of the group
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1: int, n2: int) -> bool:
            # takes two nodes, if they are connected already, return false, 
            # else union their groups
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return False
            # union their groups (by checking the size of parents)
            if size[r1] < size[r2]:
                r1, r2 = r2, r1
            par[r2] = r1
            size[r1] += size[r2]
            return True
        
        # outer loop here, looping through each edge
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
