total = int(input())

for _ in range(total):
    a,b = map(int,input().split())
    num = (a + b)//4
    print(min(num,min(a,b)))