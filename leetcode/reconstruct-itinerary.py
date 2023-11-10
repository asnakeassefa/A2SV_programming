class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse =True)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        ans = []
        def dfs(child):
            while graph[child]:
                dfs(graph[child].pop())
            ans.append(child)
        dfs('JFK')
        return ans[::-1]