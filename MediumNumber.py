T = int(input())

for _ in range(T):
    nums = list(map(int,input().split()))
    
    nums.sort()
    print(nums[1])
