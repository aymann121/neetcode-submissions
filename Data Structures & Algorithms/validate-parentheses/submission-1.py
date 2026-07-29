class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        closeToOpenMap = {'}':'{', ']':'[', ')': '('}
        for c in s:
            if c in {'(', '{', '['}:
                parenStack.append(c)
            elif parenStack and parenStack[-1] == closeToOpenMap[c]:
                parenStack.pop()
            else:
                return False
        return parenStack == []