class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-e for e in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            e1, e2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            remaining = max(e1,e2) - min(e1,e2)
            if remaining: heapq.heappush(maxHeap, -remaining)
        
        return -maxHeap[0] if maxHeap else 0