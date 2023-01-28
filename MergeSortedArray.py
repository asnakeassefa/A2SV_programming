total = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ptr1 = 0
ptr2 = 0
ans = []
while ptr2 < total[1] and ptr1 < total[0]:
    if arr1[ptr1] < arr2[ptr2]:
        ans.append(arr1[ptr1])
        ptr1 += 1
    else:
        ans.append(arr2[ptr2])
        ptr2 += 1
if ptr1 == total[0]:
    ans.extend(arr2[ptr2:])
elif ptr2 == total[1]:
    ans.extend(arr1[ptr1:])
print(*ans)
