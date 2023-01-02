class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        res = []
        for path in paths:
            Open = False
            file = path.split(' ')
            for i in range(1,len(file)):
                key = ""
                filePath = ""
                fileName = ""
                Open = False
                for item in file[i]:
                    if Open and item != ")":
                        key += item
                    elif item == "(":
                        key = ""
                        Open = True
                        continue
                    elif item == ")":
                        filePath = file[0] + "/" + fileName
                        ans[key].append(filePath)
                    else:
                        fileName += item
        for val in ans.values():
            if len(val) > 1:
                res.append(val)
        return res