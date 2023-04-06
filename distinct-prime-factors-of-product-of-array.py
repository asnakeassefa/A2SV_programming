class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1
        ans = set()
        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    num //= d
                    ans.add(d)
                d += 1
            if num > 1:
                ans.add(num)
        return len(ans)