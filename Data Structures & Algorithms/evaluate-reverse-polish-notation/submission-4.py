class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stack = []
        for t in tokens:
            if t == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(x + y)
            elif t == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif t == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x * y)
            elif t == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(t))


        return stack[-1]