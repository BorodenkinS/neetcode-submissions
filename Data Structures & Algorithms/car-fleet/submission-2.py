class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        pairs = [(position[i], speed[i]) for i in range(n)]

        pairs.sort()
        pairs.reverse()
 
        time = []

        for car in pairs:
            t = (target - car[0]) / car[1]
            if not time or time[-1] < t:
                time.append(t)

        return len(time)