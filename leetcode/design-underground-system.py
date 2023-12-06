class UndergroundSystem:

    def __init__(self):
        self.time = []
        self.check_in = defaultdict(int)
        self.stations = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = self.check_in[id][1]
        station = self.check_in[id][0]
        self.stations[(station,stationName)].append(t - time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.stations[(startStation,endStation)]
        return sum(time) / len(time)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)