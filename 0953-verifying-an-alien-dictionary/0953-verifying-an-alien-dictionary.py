from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = defaultdict(int)
        length = len(words)
        ptr1 = 0
        ptr2 = 1
        
        #coping to dictionary
        for index, char in enumerate(order):
            dic[char] = index
        # check if they are sorted
        for i in range(length-1):
            short = min(len(words[i]),len(words[i+1]))
            
            if words[i+1] in words[i] and len(words[i]) > len(words[i+1]):
                return False
            for j in range(short):
                if dic[words[i][j]] > dic[words[i+1][j]]:
                    return False
                elif dic[words[i][j]] < dic[words[i+1][j]]:
                    break
            
        return True