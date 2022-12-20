# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
k = input()
rooms = defaultdict(int)
room = list(map(int, input().split()))

for r in room:
    rooms[r] += 1

capitain = min(rooms, key=rooms.get)

print(capitain)
