class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = set(['+', '-', '*', '/'])
        stack = []

        for c in tokens:
            if c in operand:
                n2 = stack.pop()
                n1 = stack.pop()
                curr = 0
                if c == '+':
                    curr = n1 + n2
                elif c == '-':
                    curr = n1 - n2
                elif c == '*':
                    curr = n1 * n2
                else:
                    curr = int(n1 / n2)
                stack.append(curr)
            else:
                stack.append(int(c))

        return stack[0]