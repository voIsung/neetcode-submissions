class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        times = []

        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            times.append((target - p) / s)
        
        current_fleet_time = 0

        for time in times:
            if time > current_fleet_time:
                fleet_count += 1
                current_fleet_time = time

        return fleet_count