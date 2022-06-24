# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = list3node = None
        while list1 or list2:
            if not list1:
                if not list3:
                    list3 = list2
                else:
                    list3node.next = list2
                list2 = None
            elif not list2:
                if not list3:
                    list3 = list1
                else:
                    list3node.next = list1
                list1 = None
            else:
                if list1.val < list2.val:
                    if not list3:
                        list3 = ListNode(list1.val,None)
                        list3node = list3
                    else:
                        list3node.next = ListNode(list1.val,None)
                        list3node      = list3node.next
                    list1 = list1.next
                else:
                    if not list3:
                        list3 = ListNode(list2.val,None)
                        list3node = list3
                    else:
                        list3node.next = ListNode(list2.val,None)
                        list3node      = list3node.next
                    list2 = list2.next
        return list3