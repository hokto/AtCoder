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
    N,M,P = myin_sp_i()
    A = myin_sp_i()
    B = myin_sp_i()
    B.sort()
    B_accum = [0]*(M+1)
    for i in range(M):
        B_accum[i+1]=B[i] + B_accum[i]
    
    ans = 0
    for a in A:
        resi = max(P-a,0)
        ok = -1
        ng = M
        while ng-ok>1:
            m = ok+(ng-ok)//2
            if B[m]<resi:
                ok = m
            else:
                ng = m
        if ok == M:
            ans += B_accum[M]
        else:
            ans += B_accum[ok+1]+a*(ok+1)+(M-1-ok)*P
    print(ans)
        

if __name__ == "__main__":
    main()