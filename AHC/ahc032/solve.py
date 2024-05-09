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
def greedy(X):
    B = X
    KK = K 
    ans = []
    coor = []
    for s in range(N-3+1):
        for i in range(s,N-3+1):
            coor.append((i,s))
        for j in range(s,N-3+1):
            coor.append((s,j))
    for (i,j) in coor:
        best_score = -1
        best_stamp = -1
        best_stamp_cnt = -1
        for m in range(M):
            score = 0
            stamp_cnt = INF
            stamp_cnt=min(stamp_cnt,(MOD-1-B[i][j])//S[m][0][0])
            if stamp_cnt > KK:
                stamp_cnt = 0
            score += stamp_cnt*S[m][0][0]
            if best_score < score:
                best_score = score
                best_stamp = m
                best_stamp_cnt = stamp_cnt
        KK -= best_stamp_cnt
        for _ in range(best_stamp_cnt):
            ans.append([best_stamp,i,j])
            for di in range(3):
                for dj in range(3):
                    ni = i+di
                    nj = j+dj
                    B[ni][nj]=(B[ni][nj]+S[best_stamp][di][dj])%MOD
    return ans

from heapq import heapify,heappush,heappop,heappushpop
class BeamSearch:
    def __init__(self,beam_size,root,x,y):
        self.beam_size = beam_size
        self.root = root
        self.iter = 0
        self.x = x
        self.y = y
    def init(self):
        self.iter = 0
    def next(self):
        self.iter+=1
    def is_finish(self):
        return self.iter >= self.n
    def step(self,path):
        for m in range(M):
            yield m,path[:]+[m]
    def calc_score(self,prev_score,stamp):
        return (prev_score+S[stamp][0][0])%MOD
    def calc_score_upper(self,stamp):
        score = 0
        for di in range(3):
            ni = self.y+di
            nj = self.x
            score += (A[ni][nj]+S[stamp][di][0])%MOD
        return score
    def calc_score_left(self,stamp):
        score = 0
        for dj in range(3):
            ni = self.y
            nj = self.x +dj
            score += (A[ni][nj]+S[stamp][0][dj])%MOD
        return score
    def calc_score_all(self,stamp):
        score = 0
        for di in range(3):
            for dj in range(3):
                ni = self.y + di
                nj = self.x + dj
                score += (A[ni][nj]+S[stamp][di][dj])%MOD
        return score
    def solve(self,n,type=0):
        global A
        self.n = n
        if type == 0:
            paths = [(-A[self.y][self.x],self.root)]
        elif type == 1:
            score = 0
            for dj in range(3):
                nj = self.x + dj
                score += -A[self.y][nj]
            paths = [(score,self.root)]
        elif type == 2:
            score = 0
            for di in range(3):
                ni = self.y + di
                score += -A[ni][self.x]
            paths = [(score,self.root)]
        heapify(paths)
        self.init()
        while not self.is_finish():
            top_paths = []
            heapify(top_paths)
            for prev_score,path in paths:
                for use_stamp,extend_path in self.step(path):
                    if type == 0:
                        score = self.calc_score(-prev_score,use_stamp)
                    elif type == 1:
                        score = self.calc_score_upper(use_stamp)
                    elif type == 2:
                        score = self.calc_score_left(use_stamp)
                    if len(top_paths) < self.beam_size:
                        heappush(top_paths,(-score,extend_path))
                    else:
                        heappushpop(top_paths,(-score,extend_path))
            paths = top_paths
            self.next()
        result_paths = []
        result_score = -paths[0][0]
        for path in paths[0][-1]:
            result_paths.append([path,self.y,self.x])
            for di in range(3):
                for dj in range(3):
                    ni = self.y + di
                    nj = self.x + dj
                    A[ni][nj] = (A[ni][nj]+S[path][di][dj])%MOD
        return result_score,result_paths
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
    T = 10**-100
    term_cnt = 0
    for loop in range(LOOPCNT):
        score = 0
        act = random.randint(4,6)
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
                    B[pi][pj] = ((prev_b-S[stamp_idx][di][dj])%MOD+S[next_stamp_idx][di][dj])%MOD
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
                        B[pi][pj] = ((prev_b+S[stamp_idx][di][dj])%MOD-S[next_stamp_idx][di][dj])%MOD
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


def solve():
    # N=9,M=20,K=81
    #ans = greedy(A)
    global A
    ans = []
    coor = set()
    for s in range(N-3+1):
        for i in range(s,N-3):
            coor.add((i,s))
        for j in range(s,N-3):
            coor.add((s,j))
    KK = K-len(coor)
    for (i,j) in coor:
        beamsearch = BeamSearch(beam_size=20,root=[],x=j,y=i)
        score,res = beamsearch.solve(n=1)
        ans+=res
    for i in range(N-3+1):
        beamsearch = BeamSearch(beam_size=100,root=[],x=N-3,y=i)
        score,res = beamsearch.solve(n=4,type=1)
        ans+=res
    for j in range(N-3-3+1):
        beamsearch = BeamSearch(beam_size=100,root=[],x=j,y=N-3)
        score,res = beamsearch.solve(n=4,type=2)
        ans+=res
    ans = SA(ans,LOOPCNT=5*100000)
    #print(ans)
    print(len(ans))
    for output in ans:
        print(" ".join(map(str,output)))

if __name__ == "__main__":
    solve()