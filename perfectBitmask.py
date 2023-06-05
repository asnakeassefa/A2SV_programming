total = int(input())

for _ in range(total):
    ans = 0
    num = int(input())

    count = 0
    one = 0
    while not num & 1:
        count += 1
        num >>= 1
    a = 1 << count
    xor = 0
    if a == 1:
        num >>= 1
        if not num:
            xor = 2
    else:
        num >>=1
        if not num:
            xor = 1
    ans = xor + a

    print(ans)
