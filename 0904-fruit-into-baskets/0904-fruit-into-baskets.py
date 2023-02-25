class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        ans = 0
        length = len(fruits)
        fruitdict = defaultdict(int)
        
        for right in range(length):
            fruitdict[fruits[right]] = right
            if len(fruitdict) > 2:
                least = min(fruitdict.values())
                del fruitdict[fruits[least]]
                left = least
                left += 1
            ans = max(ans,right-left+1)
        return ans