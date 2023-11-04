class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        ptr = len(nums1) - 1

        while ptr1 > -1 and ptr2 > -1:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1

        while ptr1 > -1:
            nums1[ptr] = nums1[ptr1]
            ptr1 -= 1
            ptr -= 1

        while ptr2 > -1:
            nums1[ptr] = nums2[ptr2]
            ptr2 -= 1
            ptr -= 1