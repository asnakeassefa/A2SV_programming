class Solution:
    def knightDialer(self, n: int) -> int:
        dir_ = [
          (2, 1), (2, -1), (-2, 1), (-2, -1),
          (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        graph = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"],
        ]

        def dfs(node, n, memo):
          if n == 0:
            return 1
          
          if (node, n) in memo:
            return memo[(node, n)]
          
          row, col = node
          rows, cols = len(graph), len(graph[0])

          res = 0
          for r, c in dir_:
            new_row = row + r
            new_col = col + c

            if (0 <= new_row < rows and 0 <= new_col < cols) and (graph[new_row][new_col].isnumeric()):
              res += dfs((new_row, new_col), n - 1, memo)
          
          memo[(node, n)] = res
          return memo[(node, n)]
        
        res = 0
        dic = {}
        for row in range(4):
          for col in range(3):
            if graph[row][col].isnumeric():
              node = (row, col)
              res += dfs(node, n - 1, dic)
        
        return res % (10**9 + 7)