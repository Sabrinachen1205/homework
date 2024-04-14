# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        record=[]
        if not head:
            return False
        while head.next:
            record.append(head)
            if head.next in record:
                return True
            head=head.next
        return False