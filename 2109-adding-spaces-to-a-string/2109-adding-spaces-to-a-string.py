class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        index = 0
        SpaceLen = len(spaces)
        for i,char in enumerate(s):
            if index < SpaceLen and i == spaces[index]:
                answer += " " + char
                index += 1
            else:
                answer += char
                
        return answer