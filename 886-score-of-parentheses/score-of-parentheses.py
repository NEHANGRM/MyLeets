class Solution(object):
    def scoreOfParentheses(self, s):
        stack=[0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            elif ch==')':
                i=stack.pop()
                if i==0:
                    stack.append(stack.pop()+1)
                else:
                    stack.append(stack.pop()+2*i)
        return stack.pop()
        