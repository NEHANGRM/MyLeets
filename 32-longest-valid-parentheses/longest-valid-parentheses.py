class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        mc=0
        for ind,i in enumerate(s):
            if i=='(':
                stack.append(ind)
            else:
                stack.pop()
                if not stack:
                    stack.append(ind)
                else:
                    mc=max(mc,ind-stack[-1])
        return mc
            