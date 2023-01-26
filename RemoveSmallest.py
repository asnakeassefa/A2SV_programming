total = int(input())

for i in range(total):
	size = int(input())
	ans = "YES"
	nums = list(map(int,input().split()))
	nums.sort()
	for idx in range(1,size):
		if abs(nums[idx-1] - nums[idx]) > 1:
			ans = "NO"
	print(ans)
