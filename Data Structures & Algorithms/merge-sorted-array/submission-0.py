class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        i = m + n - 1

        while p1 > -1 and p2 > -1 and i > -1:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        
        while p1 > -1:
            nums1[i] = nums1[p1]
            i -= 1
            p1 -= 1
        
        while p2 > -1:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1
        