# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        l = []
        th = head

        while th != None:
            l.append(th.val)
            th = th.next

        i = 0
        s = len(l)
        j = s-1

        ans = []

        if s == 0:
            return

        elif s%2 == 0:
            while i < s//2 and j >= 0:
                ans.append(l[i])
                ans.append(l[j])
                i += 1
                j -= 1
        else:
            while i < s//2 and j >= 0:
                ans.append(l[i])
                ans.append(l[j])
                i += 1
                j -= 1
            ans.append(l[s//2])

        i = 1
        while head != None and i < s:
            head.next = ListNode(ans[i])
            head = head.next
            i += 1