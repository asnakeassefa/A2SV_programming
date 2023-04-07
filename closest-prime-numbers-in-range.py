class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right - left < 2:
            return [-1,-1]
        primes = [i % 2 for i in range(right+1)]
        primes[1] = 0
        primes[2] = 1
        d = 3
        while d * d <= right:
            if primes[d]:
                j = d * d
                while j <= right:
                    primes[j] = 0
                    j += d
            d += 2
        
        while primes[left] != 1 and left < right:
            left += 1
        ptr1 = left
        temp = [-1,-1]
        ans = float('inf')

        for ptr2 in range(left+1,right+1):
            if primes[ptr2] == 1:
                if ans > ptr2-ptr1:
                    temp = [ptr1,ptr2]
                    ans = ptr2 - ptr1
                ptr1 = ptr2
        return temp