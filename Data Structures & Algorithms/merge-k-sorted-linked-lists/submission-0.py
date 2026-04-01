# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next
        
        def merge(arr1, arr2):
            p1 = p2 = 0
            res = []

            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] > arr2[p2]:
                    res.append(arr2[p2])
                    p2 += 1
                else:
                    res.append(arr1[p1])
                    p1 += 1
            
            while p1 < len(arr1):
                res.append(arr1[p1])
                p1 += 1
            
            while p2 < len(arr2):
                res.append(arr2[p2])
                p2 += 1
            
            return res

        def mergeSort(arr):
            N = len(arr)
            if N <= 1:
                return arr
            
            return merge(mergeSort(arr[N // 2:]), mergeSort(arr[:N // 2]))
        
        sorted_arr = mergeSort(arr)

        dummy = ListNode()
        curr = dummy

        for n in sorted_arr:
            curr.next = ListNode(n)
            curr = curr.next
        
        return dummy.next