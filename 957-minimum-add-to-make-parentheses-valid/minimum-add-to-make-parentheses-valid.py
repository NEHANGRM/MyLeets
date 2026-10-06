class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')

            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')

        return len(stack)