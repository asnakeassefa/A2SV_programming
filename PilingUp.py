T = int(input())

for k in range(T):
    size = int(input())
    array = list(map(int,input().split()))
    ptr1 = 0
    ptr2 = size-1
    start = 0
    ok = True
    while(ptr1 != ptr2):
        
        if array[ptr1] > array[ptr2]:
            start = ptr1
            ptr1 += 1
            if start != 0 and array[start] < array[ptr1]:
                ok = False
                break
                
        else:
            start = ptr2
            ptr2 -= 1
            if start != 0 and array[start] < array[ptr2]:
                ok = False
                break
    if ok:
        print("Yes")
    else:
        print("No")
