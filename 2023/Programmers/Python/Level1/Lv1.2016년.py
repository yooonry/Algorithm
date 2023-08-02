# Level1 Programmers
# 04 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    count=0
    num=0
    day=['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a-1):
        count+=month[i]
    num=(count+b)%7
    return day[num]
