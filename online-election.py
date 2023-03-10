class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.arr = []
        count = defaultdict(int)
        length = len(self.persons)
        maxVal = -1
        maxKey = -1
        for i in range(length):
            count[self.persons[i]] += 1
            if maxVal <= count[self.persons[i]]:
                maxVal = count[self.persons[i]]
                maxKey = self.persons[i]
            self.arr.append(maxKey)
    
    def q(self, t: int) -> int:
        low = -1
        high = len(self.times)
        
        while low + 1 < high:
            mid = low + (high - low)//2

            if self.times[mid] <= t:
                low = mid
            else:
                high = mid
        
        return self.arr[low]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)