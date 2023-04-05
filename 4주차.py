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
  
  
#answer[-1] 쓰면 편헀다. 배열크기0에도 -1인덱스 사용가능
