class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s)-1
        left = 0
        def reverse(right,left):
            if left < right:
                s[left],s[right] = s[right],s[left]
                reverse(right-1,left+1)
        reverse(right,left)