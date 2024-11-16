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
    N,Q = myin_sp_i()
    C = myin_sp_i()
    S = [set([C[i]]) for i in range(N)]
    for q in range(Q):
        a,b = myin_sp_i()
        a-=1
        b-=1
        if len(S[a])<len(S[b]):
            for e in S[a]: S[b].add(e)
            S[a].clear()
        else:
            for e in S[b]: S[a].add(e)
            S[b].clear()
            S[a],S[b] = S[b],S[a]
        print(len(S[b]))

if __name__ == "__main__":
    main()