class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height)):
            l, r = max(height[:i]), max(height[i:])
            currWater = min(l,r) - height[i]
            if currWater > 0:
                res += currWater
        return res
            