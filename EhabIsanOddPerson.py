from collections import defaultdict

total = int(input())
nums = list(map(int,input().split()))

odd = 0
even = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if odd and even:
    nums.sort()

print(*nums)