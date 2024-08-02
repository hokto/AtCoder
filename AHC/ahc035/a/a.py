from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import random
random.seed(19970324)
import copy
def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

DIR = [[-1,0],[1,0],[0,-1],[0,1]]
def calc_exp(X,M,a1,a2):
    score = 0.0
    for m in range(M):
        score+=X[a1][m]+X[a2][m]
    return score/2

def max_exp_calc(A,X,N,M):
    best_scores = []
    for i in range(N):
        for j in range(N):
            a1 = A[i][j]
            for di,dj in DIR:
                ni = i+di
                nj = j+dj
                if not(0<=ni<=N-1 and 0<=nj<=N-1):
                    continue
                a2 = A[ni][nj]
                score = calc_exp(X,M,a1,a2)
                best_scores.append(score)
    best_scores.sort(reverse=True)
    res = 0.0
    for i in range(N*N//2):
        res+=best_scores[i]
    return res
def random_choise(A,X,N,M,best_score):
    random_indices = list(range(N*N))
    random.shuffle(random_indices)
    for idx1 in range(N*N):
        i1 = random_indices[idx1]//N
        j1 = random_indices[idx1]%N
        for idx2 in range(idx1+1,N*N):
            i2 = random_indices[idx2]//N
            j2 = random_indices[idx2]%N
            A[i1][j1],A[i2][j2] = A[i2][j2],A[i1][j1]
            score = max_exp_calc(A,X,N,M)
            A[i1][j1],A[i2][j2] = A[i2][j2],A[i1][j1]
            if best_score < score:
                return i1,j1,i2,j2,score
    return -1,-1,-1,-1,0
            
            
            
def ls(A,X,N,M):
    # 期待値の最大を計算
    best_score = max_exp_calc(A,X,N,M)
    LS_ITER = 50
    for ls_iter in range(LS_ITER):
        i1,j1,i2,j2,score = random_choise(A,X,N,M,best_score)
        if score < best_score:
            break
        best_score = score
        A[i1][j1],A[i2][j2]=A[i2][j2],A[i1][j1]
    return best_score

# k個の種配置を変更する
def kick(A,N,k):
    seeds = list(range(N*N))
    sigma = random.sample(seeds,k)
    for i in range(k-1):
        i1 = sigma[i]//N
        j1 = sigma[i]%N
        i2 = sigma[i+1]//N
        j2 = sigma[i+1]%N
        A[i1][j1],A[i2][j2] = A[i2][j2],A[i1][j1]
        
# k個の使っていない種に交換する
def kick2(A,N,k):
    used = [False] * (2*N*(N-1))
    for i in range(N):
        for j in range(N):
            used[A[i][j]]=True
    used_list = []
    unused_list = []
    for i in range(2*N*(N-1)):
        if used[i]:
            used_list.append(i)
        else:
            unused_list.append(i)
    choise_used_list = random.sample(used_list,k)
    choise_unused_list = random.sample(unused_list,k)
    exchange = {}
    for i in range(k):
        exchange[choise_used_list[i]] = choise_unused_list[i]
    for i in range(N):
        for j in range(N):
            if A[i][j] in exchange:
                A[i][j] = exchange[A[i][j]]
    
def ils(A,X,N,M):
    # 期待値の最大を計算
    best_score = max_exp_calc(A,X,N,M)
    ILS_ITER = 10
    for ils_iter in range(ILS_ITER):
        B = copy.deepcopy(A)
        kick(B,N,k=6)
        #kick2(B,N,k=2)
        score = ls(B,X,N,M)
        if best_score < score:
            best_score = score
            A = B
    return best_score
def inner_multiple(x,y,n):
    res = 0
    for i in range(n):
        res+=x[i]*y[i]
    return res
def main():
    N, M, T = myin_sp_i()
    SEED_COUNT = 2 * N * (N - 1)
    for t in range(T):
        X = []
        XX = []
        for i in range(SEED_COUNT):
            X.append(myin_sp_i())
            XX.append([sum(X[-1]),i])
        best_seed = max(XX,key=lambda x:x[0])
        XX.sort(key=lambda x:-inner_multiple(X[x[1]],X[best_seed[1]],M))
        A = [[0] * N for i in range(N)]
        idx = 0
        for n in range(N):
            A[n][0] = XX[idx][1]
            idx+=1
            for j in range(n):
                A[n][j+1]=XX[idx][1]
                idx+=1
            for i in range(n):
                A[n-1-i][n]=XX[idx][1]
                idx+=1
        ils(A,X,N,M)
        for i in range(N):
            print(' '.join(map(str, A[i])), flush=True)


    for i in range(SEED_COUNT):
        myin()


if __name__ == "__main__":
    main()