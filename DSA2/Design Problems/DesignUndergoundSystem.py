class UndergroundSystem:

    def __init__(self):
        self.checks = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checks:
            self.checks[id] = []
            self.checks[id].append([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checks:
            start, t1 = self.checks[id][0]
            if start not in self.averages:
                self.averages[start] = []
            self.averages[start].append([stationName, t - t1])
        del self.checks[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        res = []
        count = 0
        for dest, time in self.averages[startStation]:
            if endStation == dest:
                res.append(time)
                count += 1
        return sum(res) / count
