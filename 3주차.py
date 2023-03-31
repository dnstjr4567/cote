#예산
#https://school.programmers.co.kr/learn/courses/30/lessons/12982
#작은거부터 더해야 많이 담음ㅇㅇ
def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in range(len(d)):
        sum += d[i]
        answer += 1
        if sum>budget:
            answer -=1
            break
    return answer
  
#문자열 다루기 기본
#https://school.programmers.co.kr/learn/courses/30/lessons/12918
#그냥저냥
def solution(s):
    answer = True
    num = '1234567890'
    if len(s)==6: answer = True
    elif len(s)==4: answer = True
    else: answer = False
    for i in range(1,len(s)):
        if s[0] in num:
            if s[i] not in num:
                answer = False
        else : 
            if s[i] in num:
                answer = False
    return answer
  
#치킨쿠폰
#https://school.programmers.co.kr/learn/courses/30/lessons/120884
#나머지 몫 잘 이용 재밌네 
def solution(chicken):
    answer = 0
    while(True):
        a = chicken // 10
        b = chicken % 10
        answer+=a
        if a ==0:
            break
        chicken = a+b
        
    return answer
