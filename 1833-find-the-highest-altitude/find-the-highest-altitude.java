class Solution {
    public int largestAltitude(int[] gain) {
        int s=0,max=0;
        for(int i:gain)
        {
            s+=i;
            if(s>max)
            max=s;
        }
        return max;
    }
}