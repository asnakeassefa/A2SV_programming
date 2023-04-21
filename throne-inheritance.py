class ThroneInheritance:

    def __init__(self, kingName: str):
        self.store = defaultdict(list)
        self.king = kingName
        self.store[kingName] = []
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.store[parentName].append(childName)
    def death(self, name: str) -> None:
        self.dead.add(name)
    def DFS(self,store,king,dead,ans):
        if not store:
            return
        if king not in dead:
            ans.append(king)
        for val in store[king]:
            self.DFS(store,val,dead,ans)
    def getInheritanceOrder(self) -> List[str]:
        ans = []
        self.DFS(self.store,self.king,self.dead,ans)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()