from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
    X = myin_sp_i()
    invs = [[] for i in range(N)]
    for q in range(Q):
        invs[X[q]-1].append(q)
    s = [0]*Q
    for inv in invs:
        for i in range(0,len(inv),2):
            s[inv[i]]+=1
            if i+1<len(inv):
                s[inv[i+1]]-=1
    for q in range(Q-1):
        s[q+1]+=s[q]
    #print(s)
    accum = [0]*(Q+1)
    for i in range(Q):
        accum[i+1]=accum[i]+s[i]
    A = [0]*N
    for i,inv in enumerate(invs):
        for k in range(0,len(inv),2):
            l = inv[k]
            if k+1==len(inv):
                r = Q
            else:
                r = inv[k+1]
            A[i]+=accum[r]-accum[l]
    print(*A)

if __name__ == "__main__":
    main()