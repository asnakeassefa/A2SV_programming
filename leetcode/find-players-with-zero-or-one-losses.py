class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losse = defaultdict(int)
        players = set()
        for w,l in matches:
            losse[l] += 1
            players.add(w)
            players.add(l)
        ans = [[],[]]
        players = sorted(list(players))
        for player in players:
            if losse[player] == 1:
                ans[1].append(player)
            if losse[player] == 0:
                ans[0].append(player)
        return ans