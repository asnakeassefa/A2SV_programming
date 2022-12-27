# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
dic = defaultdict(list)
B = []
size = input()
lists = size.split(' ')

for i in range(int(lists[0])):
    dic[input()].append(i+1)

for i in range(int(lists[1])):
    char = input()
    B.append(char)
    if not dic[char]:
        dic[char].append(-1)

for char in B:
    for a in dic[char]:
        print(a,end = " ")
    print()
    
