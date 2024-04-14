# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1= list1
        l2= list2
        head = new_list = ListNode(0)
        while(l1 and l2):
            if (l1.val < l2.val):
                new_list.next = l1
                l1 = l1.next  
            else:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next

        new_list.next = l1 or l2
        return head.next