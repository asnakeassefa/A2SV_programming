# Enter your code here. Read input from STDIN. Print output to STDOU
from collections import defaultdict

q = list(map(int,input().split()))
n = []
A = []
B = []
nums = defaultdict(int)
happiness = 0
n = list(map(int,input().split()))
for x in n:
    nums[x] += 1

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for x in A:
    happiness += nums[x]
for x in B:
    happiness -= nums[x]

print(happiness)
