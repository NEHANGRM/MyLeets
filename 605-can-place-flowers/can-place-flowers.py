class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        c=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if ((i==0) or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                    c+=1
                    flowerbed[i]=1
        return c>=n
        