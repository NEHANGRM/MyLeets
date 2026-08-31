class Solution(object):
    def maxArea(self, height):
        m=0
        i,j=0,len(height)-1
        a=0
        while(i<len(height) and j>=0):
            a=(j-i)*min(height[i],height[j])
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            if m<a:
                m=a
        return m
        