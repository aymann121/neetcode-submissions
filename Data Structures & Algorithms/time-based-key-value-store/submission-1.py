class TimeMap:

    timeMap = {}

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def binarySearch(l,r):
            res = 0
            valid = False
            while l <= r:
                m = (l +r) //2
                if self.timeMap[key][m][0] == timestamp:
                    return m
                elif self.timeMap[key][m][0] < timestamp:
                    res = m
                    l = m +1
                    valid = True
                else:
                    r = m-1
                    res = r
            return res if valid else -1
        
        v = binarySearch(0, len(self.timeMap[key])-1)
        return self.timeMap[key][v][1] if v != -1 else ""
        
