class Solution:
    def printVertically(self, s: str) -> List[str]:
        # string = defaultdict(str)
        # maxLen = 0
        answer = []
        words = s.split(" ")
        row = len(words)
        col = 0
        for word in words:
            col = max(col,len(word))
        
        for j in range(col):
            space = ""
            temp = ""
            for i in range(row):
                if j >= len(words[i]):
                    space += " "
                else:
                    temp += space
                    space = ""
                    temp += words[i][j]
            answer.append(temp)
            
        return answer