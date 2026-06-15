class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        for i in range(len(height)):
            curr = min(max(height[:i] or [0]), max(height[i+1:] or [0])) - height[i]
            if curr > 0:
                total += curr

        return total