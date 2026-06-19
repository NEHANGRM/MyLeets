class Solution(object):
    def largestAltitude(self, gain):
        s=0
        net=[0]
        for i in gain:
            s+=i
            net.append(s)
        return max(net)
        