class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        ans = 0
        length = len(fruits)
        fruitdict = Counter()
        
        for right in range(length):
            fruitdict[fruits[right]] = right
            if len(fruitdict) > 2:
                key = min(fruitdict, key = fruitdict.get)
                least = fruitdict[key]
                del fruitdict[key]
                left = least
                left += 1
            ans = max(ans,right-left+1)
                
        return ans