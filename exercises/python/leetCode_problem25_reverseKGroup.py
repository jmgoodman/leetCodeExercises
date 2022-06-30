# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # define a method for recursively re-aliasing nodes so you can easily go back after reversing where they point
    # (note: you totally coulda just done this via a for loop and assigning to a variable "next" before back-pointing the node...)
    # this method works entirely in-place, so no output
    def recursiveTraversalAndPointBack(self,head: Optional[ListNode],k:int) -> None:
        if k < 2:
            return # don't do anything if you're trying to reverse a single node (or somehow... less?)
        
        newhead = head.next # re-aliasing
        if k > 2:
            self.recursiveTraversalAndPointBack(newhead,k-1)
        
        # flip how they point
        newhead.next = head # re-pointing
        return
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res      = ListNode()
        res.next = head
        outerleftpointer = rightpointer = res
        
        # we're gonna have a whole slew of pointers
        # outerleft: points to the element just before the target range
        # left: points to the (originally) leftmost point in the target range
        # right: points to the (originally) rightmost point in the target range
        # outerright: points to the element just after the target range
        
        while True:
            leftpointer = outerleftpointer.next
            
            # shift the rightpointer to the end of the target range
            # if you can't, you're done
            # NOTE: what is currently done by recursiveTraversalAndPointBack could totally be done in this loop no problem, and would save you a factor of 2 on execution time...
            # (...and/or might be the key to having O(1) space complexity, since your recursive method needs to store O(k) pointers in memory!)
            for _ in range(k):
                if rightpointer:                    
                    rightpointer = rightpointer.next # lefthand side is not "next", ergo this is just re-aliasing
                else:
                    return res.next # remember: res was a shell
                
            if not rightpointer:
                return res.next
            
            outerrightpointer = rightpointer.next
            
            # flip the arrangement of the target range pointers
            self.recursiveTraversalAndPointBack(leftpointer,k)
            
            # now point the outerleft pointer to the right pointer
            outerleftpointer.next = rightpointer
            
            # and point the left pointer to the outerright pointer
            leftpointer.next = outerrightpointer
            
            # now re-alias the outerleftpointer and rightpointer to the leftpointer (which now points to the first element outside the current range) to prepare for the next iteration
            outerleftpointer = rightpointer = leftpointer
            
            
            
            
