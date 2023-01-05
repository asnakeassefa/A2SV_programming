from collections import defaultdict

Total = int(input())

for i in range(Total):
	dic = defaultdict(int)
	totalPlanets,cost = list(map(int,input().split()))
	planets = list(map(int,input().split()))
	for planet in planets:
		dic[planet] += 1
	
	ans = 0
	for val in dic.values():
		ans += min(val,cost)
	print(ans)
