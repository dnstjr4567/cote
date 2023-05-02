#삼각형의 완성조건
#https://school.programmers.co.kr/learn/courses/30/lessons/120889
def solution(sides):
    sides.sort()
    if sides[0]+sides[1]>sides[2]:
        return 1
    else:
        return 2
      
#문제 그대로      
      
#콜라츠 추측
#https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    while(True):
        if num % 2 ==0:
            num = num /2
        elif num ==1 :
            return answer
        else:
            num = num*3+1
        answer += 1    
        if answer>=500:
            return -1
#문제 그대로


#하샤드 수
#https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    sum = 0
    t = x
    while(t>=10):
        sum += t%10
        t = t//10
        print(t)
    sum+=t    
    print(sum)
    if x%sum==0:
        answer = True
    else : answer = False    
    return answer
