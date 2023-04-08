class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        val = set()
        for num in edges:
            if num[0] not in val:
                val.add(num[0])
            else:
                return num[0]
            
            if num[1] not in val:
                val.add(num[1])
            else:
                return num[1]