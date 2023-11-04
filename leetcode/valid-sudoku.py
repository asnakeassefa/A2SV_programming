class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        nums = ["1","2","3","4","5","6","7","8","9"]
        for i in range(9):
            temp = defaultdict(int)
            for j in range(9):
                if board[i][j] in nums:
                    temp[board[i][j]] += 1
                if temp[board[i][j]] > 1:
                    return False
        for j in range(9):
            temp = defaultdict(int)
            for i in range(9):
                if board[i][j] in nums:
                    temp[board[i][j]] += 1
                if temp[board[i][j]] > 1:
                    return False
        temp = defaultdict(list)
        for i in range(9):
            for j in range(9):
                a = i//3
                b = j//3
                if board[i][j] in nums:
                    temp[(a,b)].append(board[i][j])
                if temp[(a,b)].count(board[i][j]) > 1:
                    return False
        return True