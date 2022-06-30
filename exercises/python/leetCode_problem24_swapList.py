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
        # okay, if you think about a graph of linked pointers
        # where all pure-name assignments establish aliases of these pointers
        # and all .next assignments establish new links between pointers
        # things start to make a lot more sense...
        # in other words, pure-name assignments move aliases around, and .next assignments move arrows around
        while head and head.next:
            first = head
            second = head.next
            
            prenode.next = second
            first.next = second.next
            second.next = first
            
            prenode = first
            head = first.next
            
        return res.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_rehearsePointerLogic:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # okay, time to deploy my own solution to this
        # think of "res" as a pointer to the value currently assigned to "head"
        res = ListNode()
        res.next = head
        
        # assign a variable "headPointer" which points to head (i.e., which gets res assigned to it)
        headPointer = res
        
        # while head both has a value and points to a valid value
        while head and head.next:
            # alias the current two values: head and the value it points to, head.next
            first  = head
            second = head.next
            
            # now we want to rearrange how things point to each other
            # first off, headPointer wants to point to second (since headPointer currently points to head, but if head and the value it points to are to be swapped...)
            headPointer.next = second
            
            # second of all, we now want first to stop pointing to second but rather to circumvent it to get to the value second is POINTING to
            first.next       = second.next
            
            # third of all, we now want second to point back to first (again, they *swap* positions, before first pointed to second, now...)
            second.next      = first
            
            # now we wanna shift things around
            # head should now point to the value that the element formerly known as "first" is NOW pointing to
            head = first.next
            
            # and, in turn, headPointer should point to where head is pointing (therefore, it should be assigned to "first", which is currently head's pointer)
            headPointer = first
            
            # and we contine along!
            
        return res.next # again, dereference res