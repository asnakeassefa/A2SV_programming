class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        length = len(skill)
        ptr1 = 0
        ptr2 = length -1
        num = skill[ptr1] + skill[ptr2]
        ans = 0
        while ptr1 < ptr2:
            if skill[ptr1] + skill[ptr2] == num:
                ans += skill[ptr1] * skill[ptr2]
                ptr1 += 1
                ptr2 -= 1
            else:
                return -1

        return ans