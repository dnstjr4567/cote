# https://school.programmers.co.kr/learn/courses/30/lessons/77884 약수의 개수와 덧셈
# 이중 반복문을 이용
def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
        cnt=0    
    return answer
  
# https://school.programmers.co.kr/learn/courses/30/lessons/70128 내적
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
  
#https://school.programmers.co.kr/learn/courses/30/lessons/120902   문자열 계산하기
def solution(my_string):
    return eval(my_string)
  
#내장 함수 활용 잘하자
