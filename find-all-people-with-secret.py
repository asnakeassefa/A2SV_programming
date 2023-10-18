class UnionFind:
    def __init__(self, size):
        self.rep = [i for i in range(size)]
        self.size = [1 for i in range(size)]
    def find(self, x):
        parent = self.rep[x]
        while parent != self.rep[parent]:
            parent = self.rep[parent]
        
        while x != parent:
            x_parent = self.rep[x]
            self.rep[x] = parent
            x = x_parent
            
        return parent
		
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        
        if self.size[x_rep] > self.size[y_rep]:
            self.rep[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]
        else:
            self.rep[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]
                
    def unUnion(self,x,y):
        self.rep[x] = x
        self.rep[y] = y
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        UF = UnionFind(n)
        UF.union(firstPerson,0)
        meetings.sort(key = lambda x:x[2])
        times = defaultdict(list)

        for meeting in meetings:
            times[meeting[2]].append(meeting)

        for key,values in times.items():
            for val in values:
                UF.union(val[0],val[1])
            length = len(values)
            for i in range(length-1,-1,-1):
                if not UF.connected(values[i][1],0):
                    UF.unUnion(values[i][0],values[i][1])

        ans = []
        for i in range(n):
            if UF.connected(i,0):   
                ans.append(i)  

        return ans