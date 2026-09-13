class Solution(object):
    def largestOverlap(self, img1, img2):
        n=len(img1)
        a=[(i,j) for i in range(n) for j in range(n) if img1[i][j]==1]
        b=[(i,j) for i in range(n) for j in range(n) if img2[i][j]==1]
        cnt=[[0]*(2*n) for _ in range(2*n)]
        m=0
        for ax,ay in a:
            for bx,by in b:
                dx=bx-ax+n
                dy=by-ay+n
                cnt[dx][dy]+=1
                m=max(m,cnt[dx][dy])
        return m
        