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
    N = int(myin())
    X = myin_sp_i()
    P = myin_sp_i()
    Q = int(myin())
    S = set()
    for x in X:
        S.add(x)
    query = []
    for q in range(Q):
        l,r = myin_sp_i()
        query.append((l,r))
        S.add(l)
        S.add(r)
    exc = {}
    M = len(S)
    for i,s in enumerate(sorted(S)):
        exc[s]=i
    XX = [0]*M
    for i,x in enumerate(X):
        XX[exc[x]]+=P[i]
    accum = [0]*(M+1)
    for i in range(M):
        accum[i+1]=accum[i]+XX[i]
    for l,r in query:
        l = exc[l]
        r = exc[r]
        print(accum[r+1]-accum[l])

if __name__ == "__main__":
    main()