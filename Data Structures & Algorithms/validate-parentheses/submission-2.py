class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        closeToOpenMap = {'}':'{', ']':'[', ')': '('}
        for c in s:
            if c in {'(', '{', '['}:
                parenStack.append(c)
            elif not (parenStack and parenStack.pop() == closeToOpenMap[c]):
                return False
        return parenStack == []