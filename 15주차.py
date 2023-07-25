https://school.programmers.co.kr/learn/courses/30/lessons/120866
안전지대
def solution(board):
    answer = 0
    queue = []
    vx = [0,0,1,1,1,-1,-1,-1]
    vy = [1,-1,0,1,-1,0,1,-1]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                queue.append((i,j))
    while len(queue)>0:
        i,j = queue.pop(0)
        for t in range(len(vx)):
            newi = i + vx[t]
            newj = j + vy[t]
            if 0<=newi<len(board) and 0<=newj<len(board[0]):
                       board[newi][newj]=1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                answer+=1
    return answer
  #너비우선탐색
https://school.programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어
def solution(s):
    answer = 0
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('four','4')
    s = s.replace('five','5')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('eight','8')
    s = s.replace('nine','9')
    s = s.replace('zero','0')
    s = int(s)
    return s
https://school.programmers.co.kr/learn/courses/30/lessons/120860
직사각형 넓이 구하기
def solution(dots):
    answer = 0
    xmax = -9999
    xmin = 9999
    ymax = -9999
    ymin = 9999
    for i in range(len(dots)):
            if xmax < dots[i][0]:
                xmax = dots[i][0]
            if xmin > dots[i][0]:
                xmin = dots[i][0]
            if ymax < dots[i][1]:
                ymax = dots[i][1]
            if ymin > dots[i][1]:
                ymin = dots[i][1]
    ylen = abs(ymax - ymin)
    xlen = abs(xmax - xmin)
    answer = ylen*xlen
    return answer
