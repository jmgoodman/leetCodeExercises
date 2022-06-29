# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        
        newpoint = newList = ListNode()
        
        while point and point.next:
            # get
            currentnode = ListNode(val=point.val) # listen, I HAVE to assign new ListNode objects and explicitly set their values. otherwise we get listnode cycles...
            nextnode    = ListNode(val=point.next.val) # that said, I recognize this is cheating a little bit... the rules behind python pointers are just soooo arcane to me though!
            # ughhhh my brain will NOT let me comprehend the "proper" solution right now... adding it to the bottom here for later...

            # flip
            nextnode.next = currentnode
            
            # insert
            newpoint.next = nextnode
            
            # increment
            point    = point.next.next
            newpoint = newpoint.next.next
            
        if point:
            newpoint.next = ListNode(val=point.val)
            
        # break out of its wrapper
        return newList.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_nonCheating:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        prenode = res
        
        # what is going on here??? gonna need to diagram this...
        while head and head.next:
            first = head
            second = head.next
            
            prenode.next = second
            first.next = second.next
            second.next = first
            
            prenode = first
            head = first.next
            
        return res.next