"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # store a dictionary from {OldNode : NewNode}
        # as we step through the "next" values
        # check the dictionary first for if a node has been created, if so, wire that one up,
        # if not, then create a new one
        # First check / create the random, then check / create the next and move the curr pointer down
        # the list

        # base case
        if not head:
            return None

        old_to_new = {}
        old = head
        new = Node(old.val)
        old_to_new[old] = new
        new_head = new
        
        while old:
            # set random
            if old.random:
                if old.random in old_to_new:
                    # ie we've already created this node
                    new.random = old_to_new[old.random]
                else:
                    # create a new node
                    print("created new ran node: ", old.random.val)
                    new.random = Node(old.random.val)
                    old_to_new[old.random] = new.random
            
            # set next
            if old.next:
                if old.next in old_to_new:
                    new.next = old_to_new[old.next]
                else:
                    # create a new node
                    print("created new next node: ", old.next.val)
                    new.next = Node(old.next.val)
                    old_to_new[old.next] = new.next

            old = old.next
            new = new.next
        print(new_head.val)
        return new_head
        # [ 3:3 7:7 5:5]
        # new = [ 3,N 7,5 ]