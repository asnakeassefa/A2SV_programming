class Solution:
    def compress(self, chars: List[str]) -> int:
        store = 0
        left = 0
        right = 0
        length = len(chars)
        ans = 0
        while right < length:
            temp = 0
            while right < length and chars[right] == chars[left]:
                temp += 1
                right += 1
            chars[store] = chars[left]
            left = right
            store += 1
            if store < length and temp > 1:
                for num in str(temp):
                    chars[store] = num
                    store += 1
        
        return store
                