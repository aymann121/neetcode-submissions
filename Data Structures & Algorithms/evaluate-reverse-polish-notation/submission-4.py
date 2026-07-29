class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            print(stack)
            if e not in {'*', "-", "/", "+"}:
                stack.append(int(e))
            elif e == "*":
                stack.append(stack.pop() * stack.pop())
            elif e == "+":
                stack.append(stack.pop() + stack.pop())
            elif e == "-":
                val2 = stack.pop()
                stack.append(stack.pop() - val2)

            elif e == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                if (val1 < 0 and val2 > 0) or (val1 > 0 and val2 < 0):
                    stack.append(-1 * int(-1 * val1 / val2))
                else:
                    stack.append(int(val1 / val2))
        return stack[0]
                