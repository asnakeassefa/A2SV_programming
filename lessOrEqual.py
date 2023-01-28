n,k = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()

ans = -1
temp = nums[k-1]
if k < n and nums[k] != temp and nums[k] > temp:
    ans = temp
elif k == n:
    ans = temp
if k == 0:
    if nums[k] > 1:
        ans = nums[k] - 1
    else:
        ans = -1
print(ans)
