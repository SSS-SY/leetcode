# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        dups=[]
        temp,val=head.next,head.val
        while temp:
            if temp.val==val and temp.val not in dups:
                dups.append(val)
            if temp.val!=val:
                val=temp.val
            temp=temp.next
        temp,pre=head.next,head
        while temp:
            if temp.val in dups:
                pre.next=temp.next
            else:
                pre=temp
            temp=temp.next
        return head if head.val not in dups else head.next