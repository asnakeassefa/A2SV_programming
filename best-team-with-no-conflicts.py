class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        length = len(scores)
        arr = [0] * length
        zipped = []
        for i in range(length):
            zipped.append((ages[i],scores[i]))
        zipped.sort(reverse = True)
        print(zipped)

        for i in range(length):
            j = i-1
            temp = 0
            while j > -1:
                if zipped[i][1] <= zipped[j][1]:
                    temp = max(temp,arr[j])
                j -= 1
            arr[i] = temp + zipped[i][1]
        return max(arr)