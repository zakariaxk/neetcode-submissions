class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = stones

        heapq.heapify_max(maxHeap)

        while(len(maxHeap) >= 2):

            first = heapq.heappop_max(maxHeap)
            second = heapq.heappop_max(maxHeap)

            if first == second:
                continue
            heapq.heappush_max(maxHeap, first - second)
        
        if maxHeap:
            return maxHeap[0]
        else:
            return 0
