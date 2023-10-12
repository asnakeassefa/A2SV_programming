class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        min_arr = [0] * length
        max_arr = [0] * length

        ans = 0
        for i in range(1,length):
            for j in range(i):
                if rating[i] < rating[j]:
                    min_arr[i] += 1
                    ans += min_arr[j]
                if rating[i] > rating[j]:
                    max_arr[i] += 1
                    ans += max_arr[j]

        return ans