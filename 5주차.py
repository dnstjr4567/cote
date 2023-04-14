#https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=python3
#삼총사

def solution(number):
    answer = 0
    sum = 0
    for i in range(2,len(number)):
        for j in range(1,i):
            for k in range(j):
                sum = number[i]+number[j]+number[k]
                if sum == 0:
                    answer+=1
                
    return answer
#from itertools import combinations 뭔지 공부 필요 처음봄
#문제는 쉬웠는데 이렇게 푸는거 아닌듯
#조합 숫자3개 고르기
