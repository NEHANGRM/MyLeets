class Solution(object):
    def compress(self, chars):
        a=0
        b=0
        while(a<len(chars)):
            ch=chars[a]
            c=0
            while(a<len(chars) and chars[a]==ch):
                c+=1
                a+=1
            chars[b]=ch
            b+=1
            if c>1:
                for i in str(c):
                    chars[b]=i
                    b+=1
        return b