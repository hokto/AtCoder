N,M,K = list(map(int,input().split()))
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
S = []
for i in range(M):
    S.append([])
    for j in range(3):
        S[i].append(list(map(int,input().split())))

MOD = 998244353
INF = K
# 左上から順にMODを超えない範囲で、1つのスタンプを押せるだけ押す
# 押すスタンプは最も得点が高くなるようなスタンプを選択する
def greedy(X,loop_cnt=1):
    KK = K 
    ans = []
    for _ in range(loop_cnt):
        for i in range(N-3+1):
            for j in range(N-3+1):
                best_score = -1
                best_stamp = -1
                best_stamp_cnt = -1
                for m in range(M):
                    score = 0
                    stamp_cnt = INF
                    stamp_cnt=min(stamp_cnt,(MOD-X[i][j])//S[m][0][0])
                    if stamp_cnt > KK:
                        stamp_cnt = 0
                    score += S[m][0][0]
                    if best_score < score:
                        best_score = score
                        best_stamp = m
                        best_stamp_cnt = stamp_cnt
                KK -= best_stamp_cnt
                for _ in range(best_stamp_cnt):
                    ans.append([best_stamp,i,j])
    return ans



def check(stamp_idx,i,j,dir):
    for di in range(3):
        for dj in range(3):
            ni = i+di+dir[0]
            nj = j+dj+dir[1]
            if 0>ni or ni>=N or 0>nj or nj>=N:
                return False
    return True

def cooling(T):
    return T*0.999
def SA(X,LOOPCNT,seed=401,term=100):
    import random,math
    random.seed(seed)
    DIR = ((1,0),(-1,0),(0,1),(0,-1))
    B = A
    x = X
    T = 10**10
    term_cnt = 0
    for loop in range(LOOPCNT):
        score = 0
        act = random.randint(0,6)
        if act <=3:
            if len(x)==0:
                continue
            # 4方向のいずれかに動かす
            idx = random.randint(0,len(x)-1)
            stamp_idx = x[idx][0]
            if check(stamp_idx,x[idx][1],x[idx][2],DIR[act]):
                pi = x[idx][1]
                pj = x[idx][2]
                ni = x[idx][1]+DIR[act][0]
                nj = x[idx][2]+DIR[act][1]
                for di in range(3):
                    for dj in range(3):
                        ii = pi+di
                        jj = pj+dj
                        prev_b = B[ii][jj]
                        B[ii][jj]=(prev_b-S[stamp_idx][di][dj])%MOD
                        score += B[ii][jj]-prev_b
                        iii = ni+di
                        jjj = nj+dj
                        next_b = B[iii][jjj]
                        B[iii][jjj]=(next_b+S[stamp_idx][di][dj])%MOD
                        score+= B[iii][jjj]-next_b

                if score>0 or math.exp(score/T)>random.random():
                    x[idx][1]+=DIR[act][0]
                    x[idx][2]+=DIR[act][1]
                    #print(f"# act0:{score}")
                else:
                    for di in range(3):
                        for dj in range(3):
                            ii = pi+di
                            jj = pj+dj
                            prev_b = B[ii][jj]
                            B[ii][jj]=(prev_b+S[stamp_idx][di][dj])%MOD
                            iii = ni+di
                            jjj = nj+dj
                            next_b = B[iii][jjj]
                            B[iii][jjj]=(next_b-S[stamp_idx][di][dj])%MOD


        elif act == 4:
            # スタンプを追加する
            if len(x)<K:
                stamp_idx = random.randint(0,M-1)
                i = -1
                j = -1
                while not check(stamp_idx,i,j,(0,0)):
                    i = random.randint(0,N-1)
                    j = random.randint(0,N-1)
                for di in range(3):
                    for dj in range(3):
                        ni = di+i
                        nj = dj+j
                        prev_b = B[ni][nj]
                        B[ni][nj]=(prev_b+S[stamp_idx][di][dj])%MOD
                        score+=B[ni][nj]-prev_b
                if score > 0 or math.exp(score/T)>random.random():
                    x.append([stamp_idx,i,j])
                    #print(f"# act4:{score}")
                else:
                    for di in range(3):
                        for dj in range(3):
                            ni = di+i
                            nj = dj+j
                            prev_b = B[ni][nj]
                            B[ni][nj]=(prev_b-S[stamp_idx][di][dj])%MOD

        elif act == 5:
            # スタンプを削除する
            if len(x)>0:
                idx = random.randint(0,len(x)-1)
                stamp_idx = x[idx][0]
                i = x[idx][1]
                j = x[idx][2]
                for di in range(3):
                    for dj in range(3):
                        ni = di+i
                        nj = dj+j
                        prev_b = B[ni][nj]
                        B[ni][nj] = (prev_b-S[stamp_idx][di][dj])%MOD
                        score+=B[ni][nj]-prev_b
                if score > 0 or math.exp(score/T)>random.random():
                    x.pop(idx)
                    #print(f"# act5:{score}")
                else:
                    for di in range(3):
                        for dj in range(3):
                            ni = di+i
                            nj = dj+j
                            prev_b = B[ni][nj]
                            B[ni][nj] = (prev_b+S[stamp_idx][di][dj])%MOD
        elif act == 6:
            # 座標を変えずにスタンプを変える
            if len(x) == 0:
                continue
            idx = random.randint(0,len(x)-1)
            next_stamp_idx = random.randint(0,M-1)
            stamp_idx = x[idx][0]
            i = x[idx][1]
            j = x[idx][2]
            for di in range(3):
                for dj in range(3):
                    pi = di+i
                    pj = dj+j
                    prev_b = B[pi][pj]
                    B[pi][pj] = (prev_b-S[stamp_idx][di][dj]+S[next_stamp_idx][di][dj])%MOD
                    score += B[pi][pj]-prev_b
            if score > 0 or math.exp(score/T)>random.random():
                x[idx][0] = next_stamp_idx
                #print(f"# act6:{score}")
            else:
                for di in range(3):
                    for dj in range(3):
                        pi = di+i
                        pj = dj+j
                        prev_b = B[pi][pj]
                        B[pi][pj] = (prev_b+S[stamp_idx][di][dj]-S[next_stamp_idx][di][dj])%MOD
                        score += B[pi][pj]-prev_b
        if term_cnt <=term:
            term_cnt+=1
        else: 
            T = cooling(T)
            term_cnt=0
        #print(f"# T:{T}")
        #print(f"# score:{score}")
        #if score<0:
            #print(f"# prob:{math.exp(score/T)}")
    return x


# K=81回叩いていく貪欲
# 選ぶスタンプは最もスコアが高くなるものを選ぶ
def greedy2(X):
    ans = []
    size = 0
    B = X
    while True:
        for i in range(N-3+1):
            for j in range(N-3+1):
                best_score = -INF
                best_stamp = -1
                for m in range(M):
                    score = 0
                    for di in range(3):
                        for dj in range(3):
                            prev_b = B[i+di][j+dj]
                            B[i+di][j+dj]=(B[i+di][j+dj]+S[m][di][dj])%MOD
                            score += B[i+di][j+dj]-prev_b
                    if best_score < score:
                        best_score = score
                        best_stamp = m
                size+=1
                ans.append([best_stamp,i,j])
                if size == K:
                    return ans


# 値の小さいものから順に押していくgreedy
def greedy3(X):
    B = []
    for i in range(N):
        for j in range(N):
            B.append([A[i][j],i,j])
    B=sorted(B,key=lambda x:x[0])
    KK = K 
    ans = []
    for (_,i,j) in B:
        best_score = -1
        best_stamp = -1
        best_stamp_cnt = -1
        while i+2>=N:
            i-=1
        while j+2>=N:
            j-=1
        for m in range(M):
            score = 0
            stamp_cnt = INF
            for di in range(3):
                for dj in range(3):
                    stamp_cnt=min(stamp_cnt,(MOD-X[i+di][j+dj])//S[m][di][dj])
            if stamp_cnt > KK:
                stamp_cnt = 0
            for di in range(3):
                for dj in range(3):
                    score += stamp_cnt*S[m][di][dj]
            if best_score < score:
                best_score = score
                best_stamp = m
                best_stamp_cnt = stamp_cnt
        KK -= best_stamp_cnt
        for _ in range(best_stamp_cnt):
            ans.append([best_stamp,i,j])
    return ans

def random_solve(X,seed=402):
    import random
    random.seed(seed)
    ans = []
    for k in range(K):
        i = -1
        j = -1
        stamp_idx = random.randint(0,M-1)
        while not check(stamp_idx,i,j,(0,0)):
            i = random.randint(0,N-1)
            j = random.randint(0,N-1)
        ans.append([stamp_idx,i,j])
    return ans

def solve():
    # N=9,M=20,K=81
    ans = greedy(A,loop_cnt=5)
    ans = SA(ans,LOOPCNT=5*100000)
    #print(ans)
    print(len(ans))
    for output in ans:
        print(" ".join(map(str,output)))

if __name__ == "__main__":
    solve()