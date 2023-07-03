#https://school.programmers.co.kr/learn/courses/30/lessons/68644
#두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sum = numbers[i]+numbers[j]
            if sum not in answer:
                answer.append(sum)
    answer.sort()
    return answer
#이중반복이면 끝

#https://school.programmers.co.kr/learn/courses/30/lessons/12911
#다음 큰 숫자
def solution(n):
    answer = 0
    binary = bin(n).count("1")
    for i in range(n+1,1000000):
        if bin(i).count("1") == binary:
            answer = i
            break
    return answer
#이진수로 변환하는 bin --> 0b 붙음, 문자열 형식임
