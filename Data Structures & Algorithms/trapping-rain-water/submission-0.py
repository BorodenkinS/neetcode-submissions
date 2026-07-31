class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0

        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i-1])
            suffix[-i-1] = max(suffix[-i], height[-i])
        
        water = 0
        print(prefix)
        print(suffix)

        for i in range(n):
            water += max(min(prefix[i], suffix[i]) - height[i], 0)

        return water