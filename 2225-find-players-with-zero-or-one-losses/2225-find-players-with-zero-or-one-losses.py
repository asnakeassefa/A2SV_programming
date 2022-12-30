class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        winners = set()
        ans = [[],[]]
        for matche in matches:
            winners.add(matche[0])
            losers[matche[1]] += 1
        
        for val in winners:
            if losers[val] == 0:
                ans[0].append(val)
        for key,val in losers.items():
            if val == 1:
                ans[1].append(key)
        
        ans[1].sort()
        ans[0].sort()
        return ans