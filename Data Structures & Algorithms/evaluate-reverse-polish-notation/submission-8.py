class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = "+-*/"
        stack = []

        for token in tokens:
            if token in operands:
                second = stack.pop()
                first = stack.pop()
                if token == "+": res = first + second
                elif token == "-": res = first - second
                elif token == "*": res = first * second
                elif token == "/": res = abs(first) // abs(second) * (1 - 2 * int(first*second < 0))
                stack.append(res)
            else:
                stack.append(int(token))

        result = stack.pop()
        return result