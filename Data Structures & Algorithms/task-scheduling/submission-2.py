class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #availbleHeap - -numremaining, task
        # cooldown - time when available, -numremaining, task
        freq = Counter(tasks)
        cooldownHeap = []
        availableHeap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(availableHeap)
        time = 0
        
        while cooldownHeap or availableHeap:
               
            while cooldownHeap and cooldownHeap[0][0] <= time:
                e = heapq.heappop(cooldownHeap)
                heapq.heappush(availableHeap, (e[1], e[2]))
            
            if availableHeap:
                task = heapq.heappop(availableHeap)
                if task[0] + 1 != 0:
                  heapq.heappush(cooldownHeap, (time + n + 1, task[0] + 1, task[1]))
            
            if cooldownHeap and not availableHeap:
                time = cooldownHeap[0][0]
            else:
                time += 1
            
        return time
            