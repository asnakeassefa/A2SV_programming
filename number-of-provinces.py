class Solution:
    def DFS(self,nums,idx,visited):
        length = len(nums)
        for i in range(length):
            if nums[idx][i] and i not in visited:
                visited.add((i))
                self.DFS(nums,i,visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = set()
        count = 0
        for i,num in enumerate(isConnected):
            if i not in visited:
                self.DFS(isConnected,i,visited)
                visited.add((i))
                count += 1
        return count