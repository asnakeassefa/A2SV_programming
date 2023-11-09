class Solution:
    def countOfAtoms(self, formula: str) -> str:
        ptr = 0
        stack = []
        temp = ''
        length = len(formula)
        cap = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        small = set(list('abcdefghijklmnopqrstuvwxyz'))
        nums = set(list('1234567890'))

        while ptr < length:
            if formula[ptr] == '(':
                stack.append(formula[ptr])
                ptr += 1
                continue
            
            if formula[ptr] == ')':
                ptr += 1
                num = ''
                while ptr < length and formula[ptr] in nums:
                    num += formula[ptr]
                    ptr += 1
                if num:
                    num = int(num)
                else:
                    num = 1
                tempStore  = []
                while stack[-1] != '(':
                    val = stack.pop()
                    tempStore.append([val[0],val[1]*num])
                stack.pop()
                stack.extend(tempStore)
                continue
            if ptr < length and formula[ptr] in nums:
                num = ''
                while ptr<length and formula[ptr] in nums:
                    num += formula[ptr]
                    ptr += 1
                elem = stack.pop()
                stack.append([elem[0],elem[1] * int(num)])
                continue
            if ptr < length and formula[ptr] in small:
                val = ''
                while ptr<length and formula[ptr] in small:
                    val += formula[ptr]
                    ptr += 1
                elem = stack.pop()
                stack.append([elem[0]+val,elem[1]])
                continue
            stack.append([formula[ptr],1])
            ptr += 1
        store = defaultdict(int)
        for key,val in stack:
            store[key] += val
        store = dict(sorted(store.items()))
        ans = ''
        for key,val in store.items():
            ans += key
            if val > 1:
                ans += str(val)
        return ans