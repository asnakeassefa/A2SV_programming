class Solution:
    def merge(self,list1,list2,ans):
        res = []
        i = 0
        j = 0
        length1 = len(list1)
        length2 = len(list2)
        nums = [0] * length1
        temp = 0
        while i < length1 and j < length2:
            if list1[i][0] > list2[j][0]:
                nums[i] += 1
                res.append(list2[j])
                j += 1
            else:
                res.append(list1[i])
                i += 1
        if i == length1:
            res.extend(list2[j:])
        else:
            res.extend(list1[i:])
        nums = list(accumulate(nums))
        for k in range(length1):
            ans[list1[k]] += nums[k]
        return res
    def mergeSort(self,nums,ans):
        length = len(nums)
        if length == 1:
            return nums
        left = self.mergeSort(nums[:length//2],ans)
        right = self.mergeSort(nums[length//2:],ans)
        res = self.merge(left,right,ans)
        return res
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = defaultdict(int)
        newNum = [(num,i) for i,num in enumerate(nums)]
        self.mergeSort(newNum,ans)
        return [ans[num] for num in newNum]