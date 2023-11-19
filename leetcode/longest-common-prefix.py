class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for word in strs:
            temp = ''
            for i,char in enumerate(word):
                if len(ans) > i and char == ans[i]:
                    temp += char
                else:
                    break
            ans = temp
        return ans
        