class UnionFind:
    def __init__(self,store):
        self.rep = store
    def find(self, x):
        if self.rep[x] == x:
            return x
        y = self.find(self.rep[x])
        self.rep[x] = y
        return y
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.rep[xrep] < self.rep[yrep]:
            self.rep[yrep] = xrep
        else:
            self.rep[xrep] = yrep
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        store = defaultdict()
        for account in accounts:
            length = len(account)
            for i in range(1,length):
                store[account[i]] = account[i]

        Unions = UnionFind(store)
        ans = defaultdict(lambda:[set(),[]])
        for account in accounts:
            length = len(account)
            for i in range(2,length):
                Unions.union(account[i],account[i-1])
        for account in accounts:
            length = len(account)
            for i in range(1,length):
                ans[Unions.find(account[i])][0].add(account[i])
                ans[Unions.find(account[i])][1] = account[0]
        res = []    
        # print(ans)
        ans = OrderedDict(sorted(ans.items()))
        for value in ans.values():
            temp = []
            temp.append(value[1])
            temp += sorted(list(value[0]))
            res.append(temp)
        
        return sorted(res)