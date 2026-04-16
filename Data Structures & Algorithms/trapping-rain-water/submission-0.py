class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        max_left = [0] * N
        max_right = [0] * N
        water = [0] * N

        for i in range(N):
            if i == 0:
                max_left[i] = height[i]
            else:
                max_left[i] = max(max_left[i-1], height[i])
        
        for i in reversed(range(N)):
            if i == N - 1:
                max_right[i] = height[i]
            else:
                max_right[i] = max(max_right[i+1], height[i])
        
        for i in range(N):
            water[i] = max(min(max_left[i], max_right[i]) - height[i], 0)
        
        return sum(water)
