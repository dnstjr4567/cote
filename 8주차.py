#최댓값과 최솟값
#https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = ''
    num = list(map(int,s.split()))
    answer += str(min(num))+ " "+ str(max(num))
    return answer
#공백 없애서 숫자로 만드는 파이썬 코드 
# c# Array.ConvertAll(ReadLine().Split(),int.Parse) 이거랑 똑같은거 파이썬도 있음


#푸드 파이트 대회
#https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = ''
    i = 1
    while (i<len(food)):
        if int(food[i])%2==1:
            food[i]-=1
        x = food[i]//2
        for j in range(x):
            answer+=str(i)
        i+=1 
    answer += str(0) + answer[::-1]       
    return answer
#대칭구조 


#총 약 1시간걸렸어요
