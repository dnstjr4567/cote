#https://school.programmers.co.kr/learn/courses/30/lessons/42748
#k번째 수
def solution(array, commands):
    answer = []
    for i in commands:
        t = array[i[0]-1:i[1]]
        t.sort()
        answer.append(t[i[2]-1])
    return answer

#한줄에 푸는 방법 있었는데 
#answer.append(array[i[0]-1:i[1]].sort()[i[2]-1])이게 아니고
#answer.append(sorted.(array[i[0]-1:i[1]])[i[2]-1])이거였다.

#https://school.programmers.co.kr/learn/courses/30/lessons/181865
#간단한 식 계산
#1분버전
def solution(binomial):
    return eval(binomial)
#3분버전
def solution(binomial):
    a = binomial.split()[0]
    op = binomial.split()[1]
    b = binomial.split()[2]
    a = int(a)
    b = int(b)
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    return result 
  
#https://school.programmers.co.kr/learn/courses/30/lessons/176963
#추억점수
def solution(name, yearning, photo):
    answer = []
    for x in photo:
        n = 0
        for i in name:
            if i in x:
                n+=yearning[name.index(i)]
        answer.append(n)   
    return answer
#딕셔너리로 풀수도 있었는데 그냥 이렇게 해봄
#세문제 다 해서 15분좀 안걸렸어요
