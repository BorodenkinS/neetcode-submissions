class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        if n == 1:
            return heights[0]

        stack = []
        left = [-1 for _ in range(n)]
        right = [n for _ in range(n)]

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)

        stack.clear()

        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]

            stack.append(i)

        area = 0

        for i in range(n):
            area = max(heights[i] * (right[i] - left[i] - 1), area)

        return area

        

            