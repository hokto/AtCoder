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
    from atcoder.dsu import DSU
    N,M,K = myin_sp_i()
    E = []
    for i in range(M):
        u,v,w = myin_sp_i()
        u-=1
        v-=1
        E.append((w,u,v))
    E.sort()
    dsu = DSU(N)
    A = myin_sp_i()
    B = myin_sp_i()
    cnt_a = [0]*N
    cnt_b = [0]*N
    for a in A:
        cnt_a[a-1]+=1
    for b in B:
        cnt_b[b-1]+=1
    ans = 0
    for w,u,v in E:
        if dsu.same(u,v): continue
        ru = dsu.leader(u)
        rv = dsu.leader(v)
        dsu.merge(u,v)
        r = dsu.leader(u)
        cnt_a[r] = cnt_a[ru]+cnt_a[rv]
        cnt_b[r] = cnt_b[ru]+cnt_b[rv]
        e = min(cnt_a[r],cnt_b[r])
        ans+=w*e
        cnt_a[r]-=e
        cnt_b[r]-=e
    print(ans)

if __name__ == "__main__":
    main()