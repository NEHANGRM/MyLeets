class Solution {
    public int maxNumberOfBalloons(String text) {
        int b=0,a=0,l=0,o=0,n=0;
        for(char i:text.toCharArray()){
            if(i=='b') b+=1;
            if(i=='a') a+=1;
            if(i=='l') l+=1;
            if(i=='o') o+=1;
            if(i=='n') n+=1;
        }
        return Math.min(Math.min(b,a),Math.min(Math.min(l/2,o/2),n));
    }
}