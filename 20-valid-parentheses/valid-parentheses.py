class Solution(object):
    def isValid(self, s):
        stack=[]
        op=''
        c=0
        for i in s:
            if i=='(':
                stack.append(')')
                c+=1
            elif i=='{':
                stack.append('}')
                c+=1
            elif i=='[':
                stack.append(']')
                c+=1
            else:
                if not stack:
                    return False
                op=stack.pop()
                if i!=op:
                    return False
                c-=1
        return c==0