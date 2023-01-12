class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        meals = defaultdict(int)
        
        ans = 0
        
        for delicious in deliciousness:
            
            for i in range(22):
            
                case = (2 ** i) - delicious
                if meals.get(case):
                    ans += meals[case]
            
            meals[delicious] += 1
        ans = ans % (10 ** 9 + 7)
        return ans