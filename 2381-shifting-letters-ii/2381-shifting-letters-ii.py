class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        newArray = [0] * (length + 1)
        
        for shift in shifts:
            if shift[2] == 0:
                newArray[shift[0]] -= 1
                newArray[shift[1]+1] += 1
            if shift[2] == 1:
                newArray[shift[0]] += 1
                newArray[shift[1]+1] -= 1
        for i in range(1,length+1):
            newArray[i] += newArray[i-1]
        
        ans = ""
        
        for index,char in enumerate(s):
            newChar = ord(char) - ord("a") + newArray[index] + 26
            newChar %= 26
            ans += chr(newChar + ord("a"))
        
        return ans