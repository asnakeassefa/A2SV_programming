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
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends