# Enter your code here. Read input from STDIN. Print output to STDOUT
#recive input
input()
List1 = set(list(map(int,input().split())))
input()
List2 = set(list(map(int,input().split())))
ans = len(List1.difference(List2))
print(ans)
