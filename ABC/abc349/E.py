A=[]
N=3
for i in range(N):
    A.append(list(map(int,input().split())))
TA = 1
AO = -1
EMP = 0
def calc(board):
    sum = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]==TA:
                sum+=A[i][j]
            if board[i][j]==AO:
                sum-=A[i][j]
    return sum>=0
def is_finish(board):
    for i in range(N):
        sum = 0
        for j in range(N):
            sum+=board[i][j]
        if sum==3:
            return True,TA
        if sum==-3:
            return True,AO
    for j in range(N):
        sum=0
        for i in range(N):
            sum+=board[i][j]
        if sum==3:
            return True,TA
        if sum == -3:
            return True,AO
    if (board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMP):
        if board[0][0]==TA:
            return True,TA
        else:
            return True,AO
    if (board[0][-1]==board[1][-2]==board[2][-3] and board[0][-1]!=EMP):
        if board[0][-1] ==TA:
            return True,TA
        else:
            return True,AO
    return False,EMP
def minmax(board,turn,d):
    if d==N*N:
        return calc(board)
    is_fin,winner = is_finish(board)
    if is_fin:
        if winner == TA:
            return True
        else:
            return False
    if turn == TA:
        is_win = False
    else:
        is_win = True
    for i in range(N):
        for j in range(N):
            if board[i][j]!=EMP:
                continue
            board[i][j] = turn 
            res = minmax(board,turn*-1,d+1)
            if turn == TA:
                is_win = (is_win or res)
            else:
                is_win = (is_win and res)
            board[i][j]=EMP
    return is_win

res=minmax([[EMP for i in range(N)]for j in range(N)],TA,0)
#print(res)
if res:
    print("Takahashi")
else:
    print("Aoki")
