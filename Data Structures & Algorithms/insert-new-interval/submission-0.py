class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        first = []
        last = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                first.append(interval)
            elif ((interval[0] <= newInterval[0] and interval[1] <= newInterval[1]) or 
                (interval[0] <= newInterval[1] and interval[1] >= newInterval[1])):
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            elif interval[0] > newInterval[1]:
                last.append(interval)

        res = []
        res.extend(first)
        res.append(newInterval)
        res.extend(last)
        return res