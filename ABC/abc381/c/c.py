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
    S = myin()
    slashs = []
    for i in range(N):
        if S[i]=="/":
            slashs.append(i)
    
    ans = 0
    for i in slashs:
        k = 1
        res = 1
        while i-k>=0 and i+k<N and S[i-k]=="1" and S[i+k]=="2":
            res+=2
            k+=1
        ans = max(ans,res)
    print(ans)

if __name__ == "__main__":
    main()