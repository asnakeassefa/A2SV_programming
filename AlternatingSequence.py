total = int(input())

for _ in range(total):
	length = int(input())
	nums = list(map(int,input().split()))
	ans = 0
	for i,num in enumerate(nums):
		if i == 0:
			val = num
			if length == 1:
				ans = val
			continue
		if num > 0 and val > 0:
			val = max(val,num)
			if length-1 == i:
				ans += val
		elif num < 0 and val <0:
			val = max(val,num)
			if length-1 == i:
				ans += val
		else:
			ans += val
			val = num
			if length-1 == i:
				ans += val

	print(ans)
