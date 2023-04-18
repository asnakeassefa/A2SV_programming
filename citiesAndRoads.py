total = int(input())

ans = 0
for _ in range(total):
    nums = list(map(int,input().split()))
    ans += nums.count(1)
print(ans//2)