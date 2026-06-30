class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        
        fleet_count = 0
        currentFleetTime = 0
        
        for pos, spd in pairs:
            finishTime = (target - pos) / spd
            if finishTime > currentFleetTime:
                fleet_count += 1
                currentFleetTime = finishTime
        
        return fleet_count