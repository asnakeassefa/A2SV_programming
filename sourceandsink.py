from collections import defaultdict

total = int(input())
store = defaultdict(int)

ans1 = []
ans2 = []
for i in range(1,total+1):
    flag = False
    nums = list(map(int,input().split()))
    for j,num in enumerate(nums):
        if num == 1:
            flag = True
        store[j+1] += num
    if not flag:
        ans1.append(i)
for key,val in store.items():
    if not val:
        ans2.append(key)

print(len(ans2),*ans2)
print(len(ans1),*ans1)