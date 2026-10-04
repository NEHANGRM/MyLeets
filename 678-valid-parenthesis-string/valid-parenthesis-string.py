class Solution(object):
    def checkValidString(self, s):
        ostack=[]
        astack=[]
        for i,ch in enumerate(s):
            if ch=='(':
                ostack.append(i)
            elif ch=='*':
                astack.append(i)
            else:
                if ostack:
                    ostack.pop()
                elif astack:
                    astack.pop()
                else:
                    return False

        while ostack and astack:
            if ostack.pop()>astack.pop():
                return False
        return not ostack