class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        presum = []
        ans = 0
        for i in range(length):
            presum.append((gas[i] - cost[i]))
        tank = 0
        for i,val in enumerate(presum):
            tank += val
            if tank < 0:
                tank = 0
                ans = i+1
        
        if sum(presum) < 0:
            return -1
        return ans