class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)

        for bill in bills:
            if bill == 5:
                count[5] += 1
            elif bill == 10:
                count[10] += 1
                if count[5] < 1:
                    return False
                count[5] -= 1
            elif bill == 20:
                if count[10] >= 1 and count[5] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] > 2:
                    count[5] -= 3
                else:
                    return False

        return True