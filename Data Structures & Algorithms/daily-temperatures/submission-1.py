class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []
        days = [0 for _ in range(n)]

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind = stack.pop()
                days[ind] = i - ind
            stack.append(i)

        return days
            