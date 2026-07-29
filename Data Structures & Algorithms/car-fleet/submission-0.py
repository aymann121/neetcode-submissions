class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, key = lambda x: x[0], reverse = True)
        endingTime = float(target - cars[0][0]) / cars[0][1]
        res = 1
        for i in range(1, len(cars)):
            if float(target - cars[i][0])/cars[i][1] <= endingTime:
                continue
            endingTime = float(target - cars[i][0])/cars[i][1]
            res += 1
        return res

