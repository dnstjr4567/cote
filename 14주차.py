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
#너무 조잡하게 풀었다
#다른 풀이는 깔끔하더라
#enumerate, cycle 이라는 함수 공부하기
https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
기능개발
def solution(progresses, speeds):
    answer = []
    idx = 0
    while True:
        cnt = 0
        for i in range(len(speeds)):
            if progresses[i]<100:
                progresses[i]+=speeds[i]
        while progresses[idx]>=100:
            cnt +=1
            idx+=1
            if idx>= len(speeds):
                break
        if cnt>0:
            answer.append(cnt)
        if idx>= len(speeds):
                break
    return answer
#굳이 idx말고 pop(0)사용해도 될듯한데 왜 안됐을까
#파이썬은 굳이 큐스택 안쓰고 리스트로 사용해도 좋군요
#추가적으로 먼저 c#으로푼 풀이 구조는 똑같다
public static int[] solution(int[] progresses, int[] speeds)
    {
        List<int> answer = new List<int>();
        int idx = 0;
        while (true)
        {
            int cnt = 0;
            for (int i = 0; i < progresses.Length; i++)
            {
                if (progresses[i] < 100)
                {
                    progresses[i] += speeds[i];
                }
            }
            while (progresses[idx] >= 100)
            {
                cnt++;
                idx++;
                if (idx >= progresses.Length)
                {
                    break;
                }
            }
            if (cnt > 0)
            {
                answer.Add(cnt);
            }
            if (idx >= progresses.Length)
            {
                break;
            }
        }
        return answer.ToArray();
    }
