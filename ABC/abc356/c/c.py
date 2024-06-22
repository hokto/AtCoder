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
    N,M,K = myin_sp_i()
    R = []
    A = [[False for i in range(N)]for j in range(M)]
    for j in range(M):
        ar = myin_sp()
        C = int(ar[0])
        for k in range(C):
            a = int(ar[1+k])
            a-=1
            A[j][a]=True
        r = ar[-1]
        if r=="o":
            R.append(True)
        else:
            R.append(False)
    ans = 0 
    for bit in range(1<<N):
        check = [0 for j in range(M)]
        for i in range(N):
            if (bit&(1<<i))>0:
                for j in range(M):
                    if A[j][i]:
                        check[j]+=1
        f = True
        for j in range(M):
            if (R[j] and check[j]<K) or (not R[j] and check[j]>=K):
                f = False
        if f:
            ans+=1 
    print(ans)

if __name__ == "__main__":
    main()