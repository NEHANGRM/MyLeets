class Solution(object):
    def removeOuterParentheses(self, s):
        stack=[]
        res=""
        for i in s:
            if i==')':
                stack.pop()
            if stack:
                res+=i
            if i=='(':
                stack.append('(')
        return res

        