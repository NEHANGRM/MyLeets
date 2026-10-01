class Solution(object):
    def processStr(self, s, k):
        l=0
        for i in s:
            if i=='*':
                if l:
                    l-=1
            elif i=='#':
                l+=l
            elif i=='%':
                continue
            else:
                l+=1
        if k+1>l:
            return '.'
        for i in reversed(s):
            if i=='*':
                l+=1
            elif i=='%':
                k=l-k-1
            elif i=='#':
                if k+1>(l+1)//2:
                    k-=l//2
                l=(l+1)//2
            else:
                if k+1==l:
                    return i
                l-=1
        return '.'

            