from collections import defaultdict

Total = int(input())

for _ in range(Total):
	ans = 0
	row,col = map(int,input().split())
	matrix = []
	for i in range(row):
		matrix.append(list(map(int,input().split())))
	ans = 0
	positiveDig = defaultdict(int)
	negativeDig = defaultdict(int)

	for i in range(row):
		for j in range(col):
			positiveDig[i+j] += matrix[i][j]
			negativeDig[i-j] += matrix[i][j]
	for i in range(row):
		for j in range(col):
			ans = max(ans,(positiveDig[i+j]+negativeDig[i-j] - matrix[i][j]))
	#printing value
	print(ans)
