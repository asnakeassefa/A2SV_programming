# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
words = defaultdict(int)
n = 0;
n = input("")
for i in range(int(n)):
    word = input("")
    words[word] += 1
print(len(words))

for word in words.values():
    print(word , end=" ")
