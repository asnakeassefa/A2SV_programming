from collections import defaultdict

def encrypted(grid):
	row = len(grid)
	col = len(grid[0])
	newWord = []
	ans = ""
	for rowidx in range(row):
		temp = []
		for colidx in range(col):
			if grid[rowidx].count(grid[rowidx][colidx]) > 1:
				temp.append("_")
			else:
				temp.append(grid[rowidx][colidx])
		newWord.append(temp)
	# print(newWord)
	for colidx in range(col):
		temp = ""
		colCount = defaultdict(int)
		for rowidx in range(row):
			colCount[grid[rowidx][colidx]] += 1
		# remove duplicate elements in col
		temp = ""
		for rowidx in range(row):
			if colCount[grid[rowidx][colidx]] > 1:
				newWord[rowidx][colidx] = "_"
	# print(newWord)
	ans = ""
	for row in range(len(newWord)):
		for col in range(len(newWord[0])):
			if newWord[row][col] != "_":
				ans += newWord[row][col]
	return ans
row,col = map(int,input().split())
grid = []
for i in range(row):
	grid.append(input())

print(encrypted(grid))
