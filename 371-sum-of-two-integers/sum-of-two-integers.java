class Solution {
    public int getSum(int a, int b) {
        int s=0,c=0;
        s=a^b;
        c=(a&b)<<1;
        return s+c;
    }
}