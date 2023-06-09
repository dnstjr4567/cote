#https://school.programmers.co.kr/learn/courses/30/lessons/12915
#문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
    strings.sort()
    num = []
    for i in range(len(strings)):
        num.append(ord(strings[i][n]))
    num.sort()
    for i in num:
        for j in range(len(strings)):
            if ord(strings[j][n]) == i and strings[j] not in answer:
                answer.append(strings[j])
    return answer
  
  #sort 안에 key 넣어서도 가능한거 알아두기
