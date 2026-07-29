class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleets = 1
        cars = sorted(zip(position, speed), key = lambda e: -e[0])
        time = (target-cars[0][0])/cars[0][1]
        for c in cars:
            if (target-c[0])/c[1] > time:
                numFleets += 1
                time = (target-c[0])/c[1]
        return numFleets
