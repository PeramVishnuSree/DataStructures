

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next

        k = len(l)
        if k % 2 == 0:
            n = (k / 2) + 1
        else:
            n = (k // 2) + 1
        n = int(n)
        lst = l[n - 1:]
        for i in range(len(lst)):
            if i == 0:
                ans = sol = ListNode(lst[i])
            else:
                ans.next = ListNode(lst[i])
                ans = ans.next

        return sol