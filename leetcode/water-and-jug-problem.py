class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if jug1 + jug2 < target:
            return False
        gcd_ = math.gcd(jug1,jug2)
        return math.gcd(gcd_,target) == gcd_