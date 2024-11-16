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
    N,M = myin_sp_i()
    X = myin_sp_i()
    cnt = [0]*N
    dist = [0]*N
    for i in range(M-1):
        x = X[i]-1
        y = X[i+1]-1
        if x>y: x,y=y,x
        dist1 = y-x
        dist2 = x+N-y
        if dist1<dist2:
            cnt[x]+=1
            cnt[y]-=1
            dist[x]+=dist1
            dist[y]-=dist1
        else:
            cnt[0]+=1
            cnt[x]-=1
            cnt[y]+=1
            dist[0]+=dist2
            dist[x]-=dist2
            dist[y]+=dist2
    accum_cnt = [0]*(N+1)
    accum_dist = [0]*(N+1)
    
    for i in range(N):
        accum_cnt[i+1]=accum_cnt[i]+cnt[i]
        accum_dist[i+1]=accum_dist[i]+dist[i]
    s = sum(accum_cnt)
    #print(s)
    ans = s*2
    for i in range(N):
        res = s+accum_cnt[i+1]*N-2*accum_dist[i+1]
        if ans>res:
            ans = res
    print(ans)

if __name__ == "__main__":
    main()