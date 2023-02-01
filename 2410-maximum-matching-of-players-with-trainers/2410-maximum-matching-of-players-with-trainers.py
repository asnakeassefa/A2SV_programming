class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        Plength = len(players)
        Tlength = len(trainers)
        
        ptr1 = 0
        ptr2 = 0
        ans = 0
        while ptr1 < Plength and ptr2 < Tlength:
            if players[ptr1] <= trainers[ptr2]:
                ans += 1
                ptr1 += 1
                ptr2 += 1
            elif players[ptr1] > trainers[ptr2]:
                ptr2 += 1
            
        return ans