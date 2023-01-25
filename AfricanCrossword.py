from collections import defaultdict
# checks the grid
def encrypted(grid):
	row = len(grid)
	col = len(grid[0])
	newWord = []
	ans = ""
	#remove duplicate elements the row
	for rowidx in range(row):
		temp = []
		for colidx in range(col):
			if grid[rowidx].count(grid[rowidx][colidx]) > 1:
				temp.append("_")
			else:
				temp.append(grid[rowidx][colidx])
		newWord.append(temp)

	# removes duplicate elements in col
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
	
	#build the answer
	ans = ""
	for row in range(len(newWord)):
		for col in range(len(newWord[0])):
			if newWord[row][col] != "_":
				ans += newWord[row][col]
	return ans

# recive testcase
row,col = map(int,input().split())
grid = []
for i in range(row):
	grid.append(input())

print(encrypted(grid))
