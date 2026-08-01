class Solution:
    def isValid(self, s: str) -> bool:
        pars = {')': '(', ']': '[', '}': '{'}

        stack = []

        for ch in s:
            if ch in pars.values():
                stack.append(ch)
            elif ch in pars.keys():
                if not stack or pars[ch] != stack.pop():
                    return False

        return not stack

