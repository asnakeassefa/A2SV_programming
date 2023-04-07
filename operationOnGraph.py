from collections import defaultdict

vertices = int(input())
total = int(input())

adjMatrix = defaultdict(list)
for _ in range(total):
    nums = list(map(int,input().split()))

    if nums[0] == 1:
        adjMatrix[nums[1]].append(nums[2])
        adjMatrix[nums[2]].append(nums[1])
    else:
        print(*adjMatrix[nums[1]])