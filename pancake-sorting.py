class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = []
        while length:
            Max = [-1,101]
            if arr[length-1] != length:
                i = 0
                while i < length:
                    if arr[i] > Max[0]:
                        Max = [arr[i],i]
                    i += 1
                ans.append(Max[1]+1)
                ans.append(length)
                temp = arr[:Max[1]+1]
                temp = temp[::-1]
                temp2 = arr[Max[1]+1:]
                arr = temp + temp2
                arr.reverse()
            arr = arr[:length-1]
            length -= 1
        return ans