class Solution:
    def DFS(self,store,idx):
        if not store[idx]:
            return
        for val in store[idx]:
            self.DFS(store,val)
            store[val] = None
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        store = [[] for i in range(n)]
        for edge in edges:
            # print(edge)
            store[edge[0]].append(edge[1])
        visited = set()
        for i in range(n):
            self.DFS(store,i)
        # print(store)
        ans = []
        for i,val in enumerate(store):
            if val:
                ans.append(i)
        return ans