class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,p3 = m-1,n-1,(len(nums1)-1)
        
        while p2 >= 0:
            if p1 == -1:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1