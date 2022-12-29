# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = input()
length = int(input())
isStrict = True
isBreaking = False
for i in range(length):
    otherSet = input().split(' ')
    if len(otherSet) >= len(setA):
        isStrict = False
        break
    for elem in otherSet:
        if elem not in setA:
            isStrict = False
            isBreaking = True
            break
    if isBreaking:
        break
if isStrict:
    print("True")
else:
    print("False")
