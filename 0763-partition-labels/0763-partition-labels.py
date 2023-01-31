class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = defaultdict(int)
        
        for i,char in enumerate(s):
            indices[char] = i
        
        length = len(s)
        
        ptr1 = 0
        ptr2 = 0
        ans = []
        while ptr1 < length:
            limit = indices[s[ptr1]]
            temp = ptr1
            while ptr2 < limit:
                limit = max(limit,indices[s[ptr2]])
                ptr1 = limit
                ptr2 += 1
            ptr1 += 1
            ans.append(ptr1 - temp)
        return ans