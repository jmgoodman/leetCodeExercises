# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.backtrack = 0
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this n = len edge case was FUCKING annoying
        
        # if the next element is "next", that's the end of the list. otherwise, keep going
        if head.next == None:
            pass
        else:
            thischild = self.removeNthFromEnd(head.next,n)
            
            # "thischild" is going to be "head.next" when the backtrack counter is not yet at the target index
            # when we finally hit that target index, "thischild" will become "head.next.next", thereby eliminating the target index
            head.next = thischild
        
        # add 1 to the backtrack counter
        self.backtrack += 1
        
        # the aforementioned rule for determining "thischild"
        if n != self.backtrack:
            return head
        else:
            return head.next