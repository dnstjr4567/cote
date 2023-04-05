#같은 숫자 싫어
#https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    n = len(arr)
    answer.append(arr.pop(0))
    for i in range(len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer
  
  
