class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        length = len(command)
        ptr1 = 0
         
        while ptr1 < length:
            if command[ptr1] == "G":
                ans += "G"
                ptr1 += 1
            elif command[ptr1] == "(":
                ptr1 += 1
                if command[ptr1] == ")":
                    ans += "o"
                    ptr1 += 1
                elif command[ptr1] == "a":
                    ans += "al"
                    ptr1 += 3
        return ans