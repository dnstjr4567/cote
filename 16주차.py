#영어끝말잇기
#https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    idx = 1
    dic = {item: 0 for item in words}
    dic[words[0]] = 1
    for i in range(1,len(words)):
        dic[words[i]]+=1
        if dic[words[i]] == 2 or words[i-1][-1] != words[i][0]:
            if (i+1)%n==0:
                answer.append(n)
            else:
                answer.append((i+1)%n)
            answer.append(idx)
            break
        if i == len(words)-1 :    
            answer.append(0)
            answer.append(0)
        if (i+1) % n == 0:
            idx += 1

    return answer
n = 2
word = ["tank", "pick"]
print(solution(n,word))
