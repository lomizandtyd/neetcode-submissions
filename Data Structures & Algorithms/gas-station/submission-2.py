"""
1 2 3 4
2 2 4 1 

-1 0 -1 3  
^
   ^
      ^  
         ^

1 0 -1  0

^ ^ ^  ^

2 0 -3  1
^ ^ ^   ^

1  2 -3 0

^  ^  ^  ^

-2 -1 3 0



"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = len(gas)-1
        end = 0
        tank = (gas[start] - cost[start])

        while start > end:
            if tank >= 0:
                tank += (gas[end] - cost[end])
                end += 1
            else:
                start -= 1
                tank += (gas[start] - cost[start])

        return start