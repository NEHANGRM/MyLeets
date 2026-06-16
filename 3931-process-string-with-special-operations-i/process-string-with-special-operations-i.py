class Solution(object):
    def processStr(self, s):
        res=""
        for i in s:
            if i=='*':
                if res!="":
                    res=res[:-1]
                else:
                    res=""
            elif i=='#':
                res+=res
            elif i=='%':
                res=res[::-1]
            else:
                res+=i
        return res
