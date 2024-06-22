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
    N,M = myin_sp_i()
    S = []
    for i in range(N):
        S.append(myin())
        
    ans = N
    for bit in range(1<<N):
        popcorn = [0 for i in range(M)]
        res = 0
        for i in range(N):
            if (bit&(1<<i))>0:
                res+=1
                for j in range(M):
                    if S[i][j]=="o":
                        popcorn[j]=1
        if sum(popcorn)!=M:
            continue
        ans = min(ans,res)
    print(ans)

if __name__ == "__main__":
    main()