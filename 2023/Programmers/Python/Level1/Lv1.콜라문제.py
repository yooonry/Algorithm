#Level1 Programmers
# 01 콜라 문제

def solution(a, b, n):
    answer = 0
    rest=0
    while n>=a:
        answer+=(n//a)*b
        n=(n%a)+(n//a)*b
        
    return answer
