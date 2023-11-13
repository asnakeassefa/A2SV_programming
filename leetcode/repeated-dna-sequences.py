class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        store = set()
        temp = ''
        ans = set()
        for char in s:
            if len(temp) < 9:
                temp += char
                continue
            temp += char
            if temp in store:
                ans.add(temp)
            store.add(temp)
            temp = temp[1:]
        return ans
            
            