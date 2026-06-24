class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    # one DS is just a dict {key : (value, index)}
    # Can we use a list that we append to (towards the right is more recent)
    # This list is a fixed length (sliding window), and we always append to the right
    # on a get() call, we also append a value to the end - when we get the KV pair, it must be in
    # the list

    # [3 1 2 5] when we append a new "get" or "put" value, we update the dicts' index, such that 
    # when we pop from the back, if its index is the end (list[0]) then we remove the KV pair, since
    # it doesn't exist in our cache anymore. If its index is a diff (more recent) value in the cache
    # then we leave it in, since we know it still exists

    # Algorithm is we have a dict from {key : (value, index)} and a deque of [keys]. Every time we 
    # put or get, we append that key to the end of our deque, update the dict keys' index to the new one
    # and then if len(deque) > cap, then pop left, and if that key's index was equal to that index (it
    # was the only one in the list) then we remove that KV pair as well -> it got kicked from the list
    # append to list -> check if over -> append to KV with last index in list as index
    # KV: {1: (10, 1), 2: (20)}
    # list: [1, 2]
    # instead of a list, an always increasing count timestamp? then for the list it must be within len - cap
    # But this means it would only delete itself on a future get, else it would just sit there

    # We CLOSE! but what does this mean that it keeps shifting? We can use a pointer!! Instead of just
    # tracking the raw value, instead we can create a node class that represents our recently used list
    # such that we can easily find the first, last, and recently used! Then, instead of reassigning our
    # pointer and leaving the old one, we just move the get(node) node to the front, and delete it from the back
    # we can also deal with tracking the first and last nodes by creating dummy nodes there, such that 
    # left.next = LRU and right.prev = MRU. Then we just need helper functions for adding and removing
    # nodes in a doubly linked list (easy) then done!
    # For a get, we get the key from our hashmap which returns a pointer to our node, which we retrieve
    # the value, then we must move this pointer to the front (it was the last used) so we delete the one
    # in place, and then add it to the front (right)
    # For a put, check if in our dict alr has it, if so, update the value and remove / add to point
    # to the new value at the right. If our dict doesn't have it, then add it to our dict, and just 
    # append it to the right.
    # Now, check the length of our dict if it is > cap, if so, remove the LRU node, get its key, then
    # del it from the dict


    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insert_mru(self, key: int, val: int) -> Node:
        node = Node(key, val)
        prv = self.right.prev
        nxt = self.right

        node.prev = prv
        node.next = nxt
        prv.next = node
        nxt.prev = node
        return node




    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            # remove it from its place, and add it to the right
            self.remove(self.cache[key])
            self.cache[key] = self.insert_mru(key, val)
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # two main cases: in the cache, not in the cache
        if key in self.cache:
            # update it
            self.remove(self.cache[key])
            self.cache[key] = self.insert_mru(key, value)
        else:
            # add it
            self.cache[key] = self.insert_mru(key, value)
            if len(self.cache) > self.cap:
                # pop from the left
                rem_key = self.left.next.key
                self.remove(self.left.next)
                del self.cache[rem_key]

        
