# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # basically, we find the kth node, then reverse from the kth node downward
        # however we also need to store the "bookends" for the group: the node right before the group
        # which will be set to the kth node at the end, and the node after the group, which will be set
        # to the first node's next
        # then we just reverse within the group, find the the kth node and once the kth node is null,
        # then we just return
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            # now reverse the list
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # now connect curr and reassign the ends
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
        return dummy.next



    
    def get_kth_node(self, curr: ListNode, k: int) -> Optional[ListNode]:
        # iterate k times down the list
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr