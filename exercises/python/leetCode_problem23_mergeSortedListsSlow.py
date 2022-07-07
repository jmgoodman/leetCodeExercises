# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class slowSolution:
    def recursiveMerge(self,lists: List[Optional[ListNode]], head:Optional[ListNode]) -> None:
        newlists = [list for list in lists if list is not None]
        if len(newlists) == 0:
            return
        
        # get the candidate values
        newvals   = [list.val for list in newlists]
        
        # get the minimum among them
        minval    = min(newvals)
        
        # get argmin (index still only returns a single index, the first one, in the case of duplicates, so no edge cases to handle here)
        minlistID = newvals.index(minval)
        
        # increment the list that spat out the smallest value
        newlists[minlistID] = newlists[minlistID].next
        
        # append to head (in-place assignment)
        head.next = ListNode(minval)
        
        # and continue
        self.recursiveMerge(newlists,head.next)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(None)
        
        self.recursiveMerge(lists,res)
        
        # handle the fact that you "wrapped" your true result in an outer node where value = None to avoid having to handle the shallowest recursive call as an edge case
        return res.next

    # TODO:
    # develop comfort with the rules by which python binds names to objects in assignments (it gets screwy when things get recursive like in linked lists... head=point=NewListNode, point = point.next, now point.next points to head.next.next, i.e., head did not move nodes with point, but both are broadly still bound to the same linked list)
    # implement a priority queue to speed things up