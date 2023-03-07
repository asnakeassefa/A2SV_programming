class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        length = len(position)
        final = zip(position,speed)
        final = sorted(final,reverse = True,key = lambda x : x[0])
        
        for val in final:
            value = target - val[0]
            times.append(value/val[1])
        stack = []
        for time in times:
            if not stack:
                stack.append(time)
            else:
                stack.append(max(stack[-1],time))
        return len(set(stack))