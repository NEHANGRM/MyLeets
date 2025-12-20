class Solution {
    public int countTriples(int n) {
        int c=0;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(Math.sqrt(i*i+j*j)<=n && Math.sqrt(i*i+j*j)%1==0)
                c+=1;
                
            }
        }
        return c;
    }
}