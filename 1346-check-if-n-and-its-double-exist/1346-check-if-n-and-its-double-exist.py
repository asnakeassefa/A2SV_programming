class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if num * 2 in arr:
                if num == 0 and arr.count(0) > 1:
                    return True
                elif num != 0:
                    return True
        return False