class Solution {
    public long solution(long num) {
        long count = 0;
        for (int i=0; i<500; i++) {
            if (num==1) {
                break;
            }
            
            else if (i==499) {
                count=-1;
                break;
            }
            
        	else if (num%2==0) {
            	num=num/2;
            	count++;
            }
        
        	else if (num%2!=0) {
                num=(num*3)+1;
            	count++;
            }
        }
        return count;
    }
}
