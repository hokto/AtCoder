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
    N = int(myin())
    A = myin_sp_i()
    r_nearest = [[-1 for i in range(10+1)]for j in range(N)]
    #l_nearest = [[-1 for i in range(10+1)]for j in range(N)]
    #for i in range(N):
        #l_nearest[i][A[i]]=i
        #if i!=N-1:
            #for j in range(10+1):
                #l_nearest[i+1][j]=l_nearest[i][j]
    for i in reversed(range(N)):
        r_nearest[i][A[i]]=i
        if i!=0:
            for j in range(10+1):
                r_nearest[i-1][j]=r_nearest[i][j]
    ans=0
    prev_l = -1
    for i in range(0,N-2):
        a = A[i]
        r_mn = N
        for a1 in range(1,10+1):
            for a2 in range(1,10+1):
                if a1-a==a2-a1:
                    m = r_nearest[i+1][a1]
                    r = -1
                    if m+1<N: r = r_nearest[m+1][a2]
                    if m==-1 or r==-1:
                        continue
                    r_mn = min(r_mn,r)
        #print((prev_l,r_mn))
        ans+=(N-r_mn)*(i-prev_l)
        if r_mn !=N:
            prev_l = i
    print(ans)
if __name__ == "__main__":
    main()