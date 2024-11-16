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
    N,Q = myin_sp_i()
    dsu = DSU(N)
    S = [[i+1] for i in range(N)]
    for q in range(Q):
        t,a,b = myin_sp_i()
        if t==1:
            a-=1
            b-=1
            if dsu.same(a,b): continue
            aa = dsu.leader(a)
            bb = dsu.leader(b)
            dsu.merge(a,b)
            S[aa]+=S[bb]
            S[aa] = sorted(S[aa],reverse=True)[:10]
            S[bb]=[]
            if dsu.leader(aa)!=aa:
                S[aa],S[bb]=S[bb],S[aa]
        else:
            a-=1
            aa = dsu.leader(a)
            if len(S[aa])<b:
                print(-1)
            else:
                print(S[aa][b-1])
        #print(S)
        

if __name__ == "__main__":
    main()