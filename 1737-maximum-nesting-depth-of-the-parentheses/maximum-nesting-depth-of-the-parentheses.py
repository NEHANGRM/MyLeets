class Solution(object):
    def maxDepth(self, s):
        stack=[]
        c,mc=0,0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append('(')
                c+=1
            elif s[i]==')':
                stack.pop()
                c-=1
            else:
                continue
            if c>mc:
                mc=c
        return mc
            
        