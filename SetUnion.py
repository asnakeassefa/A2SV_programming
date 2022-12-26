# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
List1 = set(map(int,input().split()))
input()
List2 = set(map(int,input().split()))
ans = len(List1.union(List2))

print(ans)
