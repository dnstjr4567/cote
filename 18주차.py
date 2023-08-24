#https://school.programmers.co.kr/learn/courses/30/lessons/42587
#프로세스
def solution(priorities, location):
    answer = 0
    loca = []
    for i in range(len(priorities)):
        loca.append(i)
    while priorities:
        if priorities[0] == max(priorities):
            x = priorities.pop(0)
            y = loca.pop(0)
            answer+=1
            if y==location:
                break
        else:
            x = priorities.pop(0)
            priorities.append(x)
            y = loca.pop(0)
            loca.append(y)
       
    return answer
#큐 사용 문제 요세푸스의 원과 비슷한 문제였다.
#우선순위와 처음 위치를 하나의 큐에 넣으면 더 간단하게 풀릴수도 있을듯

#https://school.programmers.co.kr/learn/courses/30/lessons/12977
#소수만들기
def solution(nums):
    answer = 0
    prime = False
    for i in range(2,len(nums)):
        for j in range(1,i):
            for k in range(0,j):
                x = nums[i]+nums[j]+nums[k]
                for m in range(2,x):
                    if x % m == 0:
                        prime = False
                        break
                    else:
                        prime = True
                if prime == True:
                    answer+=1
   
    return answer
#소수는 에라토스테네스의 채 사용하면 더 좋을 수도 있을듯하다.
#에라토스네테네스의 채는 특정 범위의 소수의 개수를 찾을때 더 유리하여 지금의 방식이 더 좋을 수도 있겠다
#반복문을 4번 사용하여 시간복잡도가 너무 크게 나온다.
#itertools 라는 모듈을 사용하면 반복을 줄일 수 있다
