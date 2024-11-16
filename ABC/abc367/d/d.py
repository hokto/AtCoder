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
    from collections import defaultdict
    N,M = myin_sp_i()
    A = myin_sp_i()
    cnt1 = [0]*M
    #cnt1[0]+=1
    s1 = 0
    for i in range(N):
        s1=(s1+A[i])%M
        cnt1[s1]+=1
    ans = 0
    for i in range(M):
        ans+=cnt1[i]*(cnt1[i]-1)//2
    s2 = 0
    #print(cnt1)
    #cnt1[0]-=1
    for i in range(N):
        #print(s1,s2)
        s2=(s2+A[i])%M
        cnt1[s2]-=1
        s1=(s1+A[i])%M
        ans+=cnt1[s1]
        
    print(ans)

if __name__ == "__main__":
    main()