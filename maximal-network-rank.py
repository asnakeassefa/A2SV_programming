class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        store = [[] for i in range(n)]
        newRoads = set()
        for road in roads:
            newRoads.add(tuple(road))
        for road in newRoads:
            store[road[0]].append(road[1])
            store[road[1]].append(road[0])
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if (i,j) in newRoads or (j,i) in newRoads:
                    ans = max(ans,len(store[i])+len(store[j])-1)
                else:
                    ans = max(ans,len(store[i])+len(store[j]))
         
        return ans