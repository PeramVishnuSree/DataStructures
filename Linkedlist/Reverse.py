# Given a linked list, return a linked list with the elements reversed

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head) :
        l = []
        rl = []

        if head == None:
            return head

        while head != None:
            l.append(head.val)
            head = head.next

        for i in range(1, len(l) + 1):
            rl.append(l[-1 * i])

        for i in range(len(rl)):
            if i == 0:
                ans = sol = ListNode(rl[i])
            else:
                ans.next = ListNode(rl[i])
                ans = ans.next

        return sol