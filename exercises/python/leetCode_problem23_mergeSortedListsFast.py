# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# use the python built-in priority queue
# (lowercase in python3)
from queue import PriorityQueue

# add the total_ordering decorator to ensure you only gotta specify __eq__ and __lt__
# one thing that throws me is that decorators do NOT have to be explicitly invoked upon function call. Gotta remember that!
# (ughhhh python does SO much nonsense under the hood... very aggravating...)
from functools import total_ordering
@total_ordering
class customTuple(tuple):
    def __init__(self,thisTuple:tuple = ()):
        super().__init__()
        self = thisTuple
    def __eq__(self,other): # no recursive type hints :( :( :(
        if len(self)==0 or len(other) == 0:
            return False
        else:
            return self[0] == other[0]

    def __lt__(self,other):
        if len(self)==0 or len(other)==0:
            return False
        else:
            return self[0] < other[0]

    def __gt__(self,other):
        if len(self)==0 or len(other)==0:
            return False
        else:
            return self[0] > other[0]
        

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # step 1: init a priority queue where the k linked lists are ordered according to their maximum entries
        # CONVENIENTLY, when python compares tuples, it does so in a hierarchical basis: the first indices are compared first, and only thereafter do other indices get compared
        # THAT SAID, I don't like relying on the internals of Python's PriorityQueue to handle the case of equal-valued root nodes across lists
        # so, imma implement a custom tuple that compares the first index and ONLY the first index
        q = PriorityQueue() # uses a min priority by default
        
        for list in lists:
            if list: # i.e., if you ain't got a null list
                q.put( customTuple( (list.val,list) ) )
        
        # assign an empty listnode to two values: one is staid, the other one does in-place operations on shared pointers
        # note: this is a "shell" node, the output will be its child
        head = point = ListNode(None)
        
        while not q.empty(): # we will fail to re-insert lists if they have been exhausted. This will be N iterations.
            val, node  = q.get() # O(1) operation for a priority queue
            point.next = node
            point      = point.next # progress to the pointer of the next node
            
            # if node has a next value, re-insert it (log k time). Otherwise, screw it
            if node.next:
                q.put( customTuple( (node.next.val,node.next) ) )
        
        # de-shell your result
        return head.next
    
    # alternatively a divide-and-conquer would also have been faster than your naive solution
    # the main reason? binary comparisons are way more efficient than taking the min() of 3+ lists
    # THAT is the crux of what's going on here.