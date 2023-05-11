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
#10분 걸렸어요
  
    
#이상한 문자 만들기
#https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)):
        if s[i] != ' ':            
            if cnt%2 == 0:
                answer+=s[i].upper()
            else:
                answer+=s[i].lower()
            cnt +=1    
        else:
            answer+=s[i]
            cnt = 0    
    return answer
#10분 걸림
#문제 잘 읽기 대문자로만 바꿔서 틀리고 문자열 기준으로 해서 틀림


#짝지어 제거하기
#https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = -1
    x = []
    for i in s:
        if len(x)==0:
            x.append(i)
        else:
            if x[-1] == i:
                x.pop(-1)
            else:
                x.append(i)
    if len(x)==0:
        answer = 1
    else:
        answer = 0
    return answer
#처음 스택 사용하여 푼 경우
#스택과 큐 두개 생각
#시간초과발생 
def solution(s):
    answer = -1
    s = list(s)
    x = []
    x.append(s[0])
    s.pop(0)
    while len(s)!=0:
        if len(x)==0:
            x.append(s[0])
            s.pop(0) 
        if x[-1]==s[0]:
            x.pop(-1)
            s.pop(0)
        else:
            x.append(s[0])
            s.pop(0)   
    if len(x)==0:
        answer = 1
    else:
        answer = 0
    return answer
#스택개념떠올린것 잘했다
#효율성 측면에서 오래 걸렸다
#40분 정도 걸렸어요





