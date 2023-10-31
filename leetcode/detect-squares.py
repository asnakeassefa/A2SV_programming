class DetectSquares:

    def __init__(self):
        self.row = defaultdict(set)
        self.col = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        # self.row[point[0]].add(tuple(point))
        # self.col[point[1]].add(tuple(point))

    # def distance(self,point1,point2):
    #     return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

    # def count(self, point: List[int]) -> int:
    #     res = 0
    #     for x,y in self.row[point[0]]:
    #         distance = self.distance(point,(x,y))
    #         for a,b in self.col[point[1]]:
    #             if distance == self.distance(point,(a,b)) and (a,y) in self.points:
    #                 res = self.points[(x,y)] * self.points[(a,b)] * self.points[(a,y)]

    def count(self, point: List[int]) -> int:
        ans = 0
        for (x,y),val in self.points.items():
            if x == point[0] or abs(x-point[0]) != abs(y-point[1]):
                continue
            ans += val * self.points[(x,point[1])] * self.points[(point[0],y)]
        return ans


            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)