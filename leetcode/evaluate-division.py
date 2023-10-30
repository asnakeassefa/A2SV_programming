class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        symbols = set()
        for equation in equations:
            symbols.add(equation[0])
            symbols.add(equation[1])

        arr = {node:{symbol:float('inf') for symbol in symbols} for node in symbols}
        for symbol in symbols:
            arr[symbol][symbol] = 1

        for i,equation in enumerate(equations):
            arr[equation[0]][equation[1]] = values[i]
            arr[equation[1]][equation[0]] = 1/values[i]
        for k in symbols:
            for i in symbols:
                for j in symbols:
                    if arr[i][k] * arr[k][j] < arr[i][j]:
                        arr[i][j] = arr[i][k] * arr[k][j]
            
        ans = []
        for query in queries:
            if (query[0] not in symbols) or (query[1] not in symbols) or arr[query[0]][query[1]] == inf:
                ans.append(-1)
            else:
                
                ans.append(arr[query[0]][query[1]])
        return ans