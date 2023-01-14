class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        balles = []
        
        for i,num in enumerate(boxes):
            if num == "1":
                balles.append(i)
        boxLen = len(boxes)
        for i in range(boxLen):
            val = 0
            for num in balles:
                val += abs(num - i)
            
            answer.append(val)
            
        return answer