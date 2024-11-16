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
    S = myin()
    L = len(S)
    cnt = [[0]*26 for i in range(L+1)]
    for i in range(L)[::-1]:
        order = ord(S[i])-ord("a")
        for j in range(26):
            if order==j:
                cnt[i][j]=cnt[i+1][j]+1
            else:
                cnt[i][j]=cnt[i+1][j]
    ans = 0
    same = False
    for i in range(L):
        order = ord(S[i])-ord("a")
        if cnt[i+1][order]>0 and not same:
            same = True
            ans+=1
        ans+=sum(cnt[i+1])-cnt[i+1][order]
    print(ans)

if __name__ == "__main__":
    main()