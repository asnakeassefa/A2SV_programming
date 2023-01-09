class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evenSum = 0
        #bulding even sum
        for num in nums:
            if num % 2 == 0:
                evenSum += num
        # changing nums value
        for query in queries:
            if nums[query[1]] % 2 == 0:
                evenSum -= nums[query[1]]
            nums[query[1]] += query[0]
            
            if nums[query[1]] % 2 == 0:
                evenSum += nums[query[1]]
            ans.append(evenSum)
        return ans