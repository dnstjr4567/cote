#크기가 작은 부분 문자열
#https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    x = 0
    for i in range(len(t)-len(p)+1):
        x  = int(t[i:i+len(p)])
        print(x)
        if int(x)<=int(p):
            answer+=1
    return answer
#슬라이싱 
#15분 걸렸어요
  
