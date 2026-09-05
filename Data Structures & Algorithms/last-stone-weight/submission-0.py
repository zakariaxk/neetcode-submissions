class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0
        
        while len(stones) > 1:
            stones.sort()

            first = stones.pop()
            second = stones.pop()

            if first != second:
                stones.append(first - second)
            
            
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
        

