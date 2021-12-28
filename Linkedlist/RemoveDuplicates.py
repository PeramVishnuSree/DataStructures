# Given the head of a linked list, return a linked list with all the duplicate elements removed

 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def deleteDuplicates(self, head) :

        if head == None:
            return head

        last = head.val
        sol = ans = ListNode(head.val)

        while head != None:
            if head.val == last:
                head = head.next

            else:
                ans.next = ListNode(head.val)
                last = head.val
                head = head.next
                ans = ans.next

        return sol