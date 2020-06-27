class Solution:
    # 递归
    # 时间复杂度：O(n + m)
    # 空间复杂度：O(n + m)
    def mergeTwoLists_1(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val >= l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

    # 迭代
    # 时间复杂度：O(n + m)
    # 空间复杂度：O(1)
    def mergeTwoLists_2(self, l1, l2):
        dummy = ListNode(-1)
        pre = dummy
        while l1 and l2:
            if l1.val >= l2:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return dummy.next

    # 迭代
    # 时间复杂度：O(n + m)
    # 空间复杂度：O(1)
    def mergeTwoLists_2(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        cur.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                temp = l2.next
                l2.next = nxt
                l2 = temp
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next




