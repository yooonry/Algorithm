## Level1 Programmers
* 01 평균구하기
```java
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        for (int i=0; i<arr.length; i++) {
            answer+=arr[i];
        }
        return answer/arr.length;
    }
}
```

* 02 짝수와 홀수
```java
class Solution {
    public String solution(int num) {
        String answer = "";
        if (num%2==0)
            answer="Even";
        else
            answer="Odd";
        return answer;
    }
}
```

* 03 약수의 합
```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<=n; i++) {
            if (n%i==0)
                answer+=i;
        }
        return answer;
    }
}
```

* 04 나머지가 1이 되는 수 찾기
```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=2; i<n; i++) {
            if (n%i==1) {
                answer=i;
                break;
            }
        }
        return answer;
    }
}
```

* 05 x만큼 간격이 있는 n개의 숫자
```java
class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long [n];
        answer[0]=x;
        for (int i=1; i<n; i++) {
            answer[i]=answer[i-1]+x;        
        }
        return answer;
    }
}
```


* 06 정수 제곱근 판별
```java
class Solution {
    public double solution(double n) {
        double answer = 0;
        if (n%Math.sqrt(n)==0)
            answer=Math.pow(Math.sqrt(n)+1, 2);
        else
            answer=-1;
        return answer;
    }
}
```

* 07 문자열 내 p와 y의 개수
```java
class Solution {
    boolean solution(String s) {
        String sLower=s.toLowerCase();
        int p=0, y=0;

        for (int i=0; i<s.length(); i++) {
            if (sLower.charAt(i)=='p')
                p++;
            
            else if (sLower.charAt(i)=='y')
                y++;
        }
        
        if (p==y)
            return true;
        
        else
            return false;
    }
}
```

* 08 문자열 정수로 바꾸기
```java
class Solution {
    public int solution(String s) {
        int answer = Integer.valueOf(s);
        return answer;
    }
}
```

* 09 음양 더하기
```java
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;

        for (int i=0; i<absolutes.length; i++) {
            if (signs[i]==true) 
                answer+=absolutes[i];
            
            else 
                answer-=absolutes[i];
        }
        return answer;
    }
}
```

* 10 두 정수 사이의 합
```java
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int temp=0;
        if (a>b) {
            temp=a;
            a=b;
            b=temp;
        }
        
        for (int i=a; i<=b; i++) {
            answer+=i;
        }
        return answer;
    }
}
```

* 11 없는 숫자 더하기
```java
class Solution {
    public int solution(int[] numbers) {
        int sum=0;

        for (int i=0; i<numbers.length; i++)
            sum+=numbers[i];

        return 45-sum;
    }
}
```

* 12 콜라츠 추측
```java
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
```

* 13 서울에서 김서방 찾기
```java
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        for (int i=0; i<seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                answer="김서방은 " + i + "에 있다";
            }
        }
        return answer;
    }
}
```

* 14 핸드폰 번호 가리기
```java
class Solution {
    public String solution(String phone_number) {
        String answer = "";

        for (int i=0; i<phone_number.length()-4; i++) {
            answer+="*";
        }
        
        answer+=phone_number.substring(phone_number.length()-4, phone_number.length());
        return answer;
    }
}
```

* 15 가운데 글자 가져오기
```java
class Solution {
    public String solution(String s) {
        String answer = "";
        if (s.length()%2==0) 
            answer=s.substring((s.length()/2)-1, (s.length()/2)+1);
        
        else 
            answer=s.substring(s.length()/2, s.length()/2+1);

        return answer;
    }
}
```

* 16 수박수박수박수
```java
class Solution {
    public String solution(int n) {
        String answer = "";
        for (int i=1; i<=n; i++) {
            if (i%2==0)
                answer+="박";
                
            else
                answer+="수";
        }
        return answer;
    }
}
```

* 17 내적
```java
class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for (int i=0; i<a.length; i++) {
            answer+=a[i]*b[i];
        }
        return answer;
    }
}
```

* 18 부족한 금액 계산하기
```java
class Solution {
    public long solution(int price, int money, int count) {
        long cost=0;
        
        for (int i=1; i<=count; i++) {
            cost+=price*i;
        }
        
        if (money>cost)
            return 0;
        
        else
            return cost-money;
    }
}
```