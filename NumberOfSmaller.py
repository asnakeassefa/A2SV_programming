total = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
 
ptr1 = 0
ptr2 = 0
ans = []
while ptr2 < total[1]:
	while ptr1 < total[0] and arr1[ptr1] < arr2[ptr2]:
		ptr1 += 1
	ans.append(ptr1)
	ptr2 += 1
print(*ans)
