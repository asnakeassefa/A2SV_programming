class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        length = len(words)
        for word in words:
            temp = 0
            for char in word:
                num = 1
                shift = (ord(char)-97)+1
                print(shift)
                num <<= shift
                temp |= num
            arr.append(temp)
        ans = 0
        for i,num in enumerate(arr):
            for j in range(i+1,length):
                if not (num & arr[j]):
                    ans = max(ans,len(words[i]) * len(words[j]))
        return ans