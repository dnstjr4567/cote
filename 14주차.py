#https://school.programmers.co.kr/learn/courses/30/lessons/120908
#문자열 안에 문자열
def solution(str1, str2):
    answer = 2
    if str2 in str1:
        answer = 1
    return answer
#https://school.programmers.co.kr/learn/courses/30/lessons/42840
#모의고사
def solution(answers):
    answer = []
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    idx1 = 0
    idx2 = 0
    idx3 = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if(answers[i] == man1[idx1]):
            cnt1+=1
    
        if(answers[i] == man2[idx2]):
            cnt2+=1
            
        if(answers[i] == man3[idx3]):
            cnt3+=1
        idx1+=1
        idx2+=1
        idx3+=1
        if(idx1>=len(man1)):
                idx1 = 0
        if(idx2>=len(man2)):
                idx2 = 0
        if(idx3>=len(man3)):
                idx3 = 0
    answer.append(cnt1)
    answer.append(cnt2)
    answer.append(cnt3)
    #print(cnt1)
    #print(cnt2)
    #print(cnt3)
    ans = []
    max = -1
    for i in range(len(answer)):
        if answer[i]>max:
            max = answer[i]
            ans.clear()
            ans.append(i+1)
        elif answer[i] == max:
            ans.append(i+1)
    return ans
