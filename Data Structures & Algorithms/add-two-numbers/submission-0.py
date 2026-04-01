class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        
        p1 = 1
        while l1:
            n1 += l1.val * p1
            p1 *= 10
            l1 = l1.next
        
        p2 = 1
        while l2:
            n2 += l2.val * p2
            p2 *= 10
            l2 = l2.next
        
        resNum = n1 + n2
        if resNum == 0: return ListNode(0)
        res = None
        tail = None

        while resNum > 0:
            cur_num = resNum % 10
            resNum //= 10
            curr = ListNode(cur_num)
            if not res:
                res = curr
                tail = res
            else:
                tail.next = curr
                tail = tail.next

        return res