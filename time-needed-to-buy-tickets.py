class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        value = tickets[k]

        for index,ticket in enumerate(tickets):
            if ticket >= value and index <= k:
                ans += value
            elif ticket >= value and index > k:
                ans += value - 1
            else:
                ans += ticket
        return ans