class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = defaultdict(int)
        even = defaultdict(int)

        evenOdd = [even,odd]

        for i,num in enumerate(nums):
            evenOdd[i%2][num] += 1
        odd = dict(sorted(odd.items(), key = lambda x:x[1]))
        even = dict(sorted(even.items(), key = lambda x:x[1]))
        fomax = (0,0)
        femax = (0,0)
        if odd:
            fomax = odd.popitem()
        if even:
            femax = even.popitem()
        somax = (0,0)
        semax = (0,0)
        if  fomax[1] == femax[1] and fomax[0] == femax[0]:
            if odd:
                somax = odd.popitem()
            if even:
                semax = even.popitem()

            if somax[1] > semax[1]:
                fomax = somax
            else:
                femax = semax
        elif fomax[1] > femax[1] and fomax[0] == femax[0]:
            if odd:
                somax = odd.popitem()
            if even:
                semax = even.popitem()

            if abs(fomax[1] - somax[1]) > abs(femax[1] - semax[1]):
                femax = semax
            else:
                fomax = somax
        elif fomax[1] < femax[1] and fomax[0] == femax[0]:
            if odd:
                somax = odd.popitem()
            if even:
                semax = even.popitem()
            if abs(fomax[1] - somax[1]) < abs(femax[1] - semax[1]):
                fomax = somax
            else:
                femax = semax
        count = 0
        for i,num in enumerate(nums):
            if i % 2:
                if num != fomax[0]:
                    count += 1
            else:
                if num != femax[0]:
                    count += 1
        # count = 0
        return count