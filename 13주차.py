#https://school.programmers.co.kr/learn/courses/30/lessons/12914
#멀리 뛰기
def solution(n):
    if n==1 or n==0:
        return n
    fibo = [0]*(n+1)
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 2
    for i in range(3,n+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
    answer = fibo[n]%1234567
    return answer
#피보나치 수열
#재귀함수 쓰면 시간초과던데
#동적계획법 사용
#동적계획법 복습 필요    
    
