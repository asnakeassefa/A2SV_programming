class Solution:
    def Counter(self,list1,list2):
        ans = [0]
        i = 0
        temp = 0
        for num in list1:
            while i < len(list2) and num > list2[i] * 2:
                temp += 1
                i += 1
            ans.append(temp)
        return sum(ans)
    def merge(self,list1,list2):
        new = []
        length1 = len(list1)
        length2 = len(list2)
        minimum = min(length1,length2)
        i = 0
        j = 0
        while i < length1 and j < length2:
            if list1[i] <= list2[j]:
                new.append(list1[i])
                i += 1
            else:
                new.append(list2[j])
                j += 1
        if i == length1:
            new.extend(list2[j:])
        else:
            new.extend(list1[i:])
        return new
    def mergeSort(self,nums):
        length = len(nums)
        if length == 1:
            return nums
        left = self.mergeSort(nums[:length//2])
        right = self.mergeSort(nums[length//2:])
        self.ans += self.Counter(left,right)
        ans = self.merge(left,right)
        return ans
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        print(self.mergeSort(nums))
        return self.ans