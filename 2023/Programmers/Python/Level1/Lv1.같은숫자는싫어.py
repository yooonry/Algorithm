# Level1 Programmers
# 05 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    temp=[]
    temp.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            temp.append(arr[i])
            
    return temp
