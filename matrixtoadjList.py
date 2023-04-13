from collections import defaultdict

total = int(input())
ans = defaultdict(list)
for i in range(1,total+1):
    nums = list(map(int,input().split()))
    for j,num in enumerate(nums):
        if num == 1:
            ans[i].append(j+1)

for val in ans.values():
    print(len(val),*val)