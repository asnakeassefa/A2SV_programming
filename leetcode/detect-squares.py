class DetectSquares:

    def __init__(self):
        self.row = defaultdict(set)
        self.col = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.row[point[0]].add(tuple(point))
        self.col[point[1]].add(tuple(point))

    def distance(self,point1,point2):
        return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

    def count(self, point: List[int]) -> int:
        res = 0
        for x,y in self.row[point[0]]:
            if point[1] == y:continue
            distance = self.distance(point,(x,y))
            for a,b in self.col[point[1]]:
                if distance == self.distance(point,(a,b)) and (a,y) in self.points:
                    res += self.points[(x,y)] * self.points[(a,b)] * self.points[(a,y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)