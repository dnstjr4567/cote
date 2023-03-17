#https://school.programmers.co.kr/learn/courses/30/lessons/120585
#머쓱
def solution(array, height):
    answer = 0
    for x in array:
        if x>height:
            answer+=1
    return answer
    
#https://school.programmers.co.kr/learn/courses/30/lessons/86051    
#없는숫자
def solution(numbers):
    answer = 45
    for x in numbers:
        answer = answer-x
    return answer
    
#https://school.programmers.co.kr/learn/courses/30/lessons/76501
#음양더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]==True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
