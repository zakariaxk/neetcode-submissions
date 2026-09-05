class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = []

        for stone in stones:
            maxHeap.append(-stone)

        heapq.heapify(maxHeap)

        while(len(maxHeap) >= 2):

            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if first == second:
                continue
            heapq.heappush(maxHeap, (first - second))
        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
