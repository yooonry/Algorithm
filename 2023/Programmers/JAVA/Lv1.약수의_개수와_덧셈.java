class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        int sum=((1+right-left)*(left+right))/2;
        
        for (int i=left; i<=right; i++) {
            int count=0;
            for (int j=1; j<=i; j++) {
                if (i%j==0)
                    count++;
            }
            if (count%2!=0) {
                answer+=i;
            }
        }
        return sum-(2*answer);
    }
}
