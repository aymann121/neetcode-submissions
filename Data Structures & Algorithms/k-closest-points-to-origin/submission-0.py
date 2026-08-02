class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i,j):
            return math.sqrt(i**2 + j**2)
        heap = []

        for point in points:
            dist = -1 * distance(point[0], point[1])
            if len(heap) < k :
                heapq.heappush(heap, (dist, point[0],point[1]))
            elif dist > heap[0][0]:
                heapq.heappush(heap, (dist, point[0],point[1]))
                heapq.heappop(heap)

        res = []
        for e in heap:
            res.append([e[1],e[2]])
        return res
                