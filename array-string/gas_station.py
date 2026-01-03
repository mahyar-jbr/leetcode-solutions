# 134. Gas Station
# Time: O(n) | Space: O(1)
# Greedy: if you fail from start A at position B, start from B+1

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0    
        current_tank = 0  
        start = 0         
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                current_tank = 0
                start = i + 1
        
        if total_tank < 0:
            return -1
        else:
            return start