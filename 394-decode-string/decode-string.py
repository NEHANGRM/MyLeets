class Solution(object):
    def decodeString(self, s):
        st=[]
        curr_st=""
        curr_num=0
        for i in s:
            if i.isdigit():
                curr_num=curr_num*10+int(i)
            elif i == '[':
                st.append((curr_st,curr_num))
                curr_st=""
                curr_num=0
            elif i == ']':
                prev_st,n=st.pop()
                curr_st=prev_st+(curr_st*n)
            else:
                curr_st+=i
        return curr_st


        