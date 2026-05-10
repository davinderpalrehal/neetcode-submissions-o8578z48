# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr_list = []

        curr = head

        while curr:
            arr_list.append(curr.val)
            curr = curr.next
        
        N = len(arr_list)
        l, r = 0, N - 1
        res = 0

        while l < r:
            res = max(res, arr_list[l] + arr_list[r])
            l += 1
            r -= 1

        return res