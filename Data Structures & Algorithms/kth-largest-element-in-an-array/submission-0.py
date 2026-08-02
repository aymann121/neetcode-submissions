class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for e in nums:
            if len(heap) <k:
                heapq.heappush(heap,e)
            elif heap[0] < e:
                heapq.heappop(heap)
                heapq.heappush(heap,e)
        return heap[0]

        