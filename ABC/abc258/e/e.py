from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    N,Q,X = myin_sp_i()
    W = myin_sp_i()
    accum = [0]*(N+1)
    for i in range(N):
        accum[i+1]=accum[i]+W[i]
    G = [-1]*N
    box_cnt = [0]*N
    walk = []
    walk_idx = [-1]*N
    loop_start_idx = -1
    loop_size = 0
    def f(i,j,x):
        # i~i+j(mod N)までの和がx以上かどうか
        if i+j<N:
            return accum[i+j+1]-accum[i]>=x
        else:
            s1 = accum[N]-accum[i]
            s2 = accum[(i+j)%N+1]
            return s1+s2>=x
    i = 0
    while G[i]==-1:
        s = X//accum[-1]
        r = X%accum[-1]
        box_cnt[i]=s*N
        ng = -1
        ok = N
        if r==0:
            ok = -1
        else:
            while ok-ng>1:
                m = ng+(ok-ng)//2
                if f(i,m,r):
                    ok = m
                else:
                    ng = m
        box_cnt[i]+=ok+1
        G[i] = (i+ok+1)%N
        walk_idx[i] = len(walk)
        walk.append(i)
        i = (i+ok+1)%N
    loop_start_idx = walk_idx[i]
    loop_size = len(walk) - walk_idx[i]
    for q in range(Q):
        K = int(myin())
        K-=1
        if K<loop_start_idx:
            print(box_cnt[walk[K]])
        else:
            K-=loop_start_idx
            K%=loop_size
            print(box_cnt[walk[loop_start_idx+K]])

if __name__ == "__main__":
    main()