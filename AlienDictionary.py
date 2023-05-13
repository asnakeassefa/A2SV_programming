#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def getChild(self,word1,word2,store):
        length = min(len(word1),len(word2))
        for i in range(length):
            if word1[i] != word2[i]:
                store[word1[i]].add(word2[i])
                return
        
    def findOrder(self,alien_dict, N, K):
    # code here
        store = defaultdict(set)
        for i in range(N-1):
            self.getChild(alien_dict[i],alien_dict[i+1],store)
        
        indeg = defaultdict(int)
        
        for i in range(K):
            indeg[chr(ord('a') + i)]
        for key,values in store.items():
            for val in values:
                indeg[val] += 1
        queue = deque()
        
        for key,val in indeg.items():
            if val == 0:
                queue.append(key)
        topSort = ""
        # print(store)
        while queue:
            node = queue.popleft()
            topSort += node
            for val in store[node]:
                indeg[val] -= 1
                if indeg[val] == 0:
                    queue.append(val)
        
        return topSort
        