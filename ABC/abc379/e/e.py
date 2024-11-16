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
    ans = [0]*(N+6)
    digit_sum = 0
    for i in range(N):
        digit_sum+=int(S[i])*(i+1)
    for i in range(N):
        tmp = digit_sum
        j =0
        while tmp:
            ans[i+j]+=tmp%10
            tmp//=10
            if ans[i+j]>=10:
                ans[i+j]-=10
                tmp+=1
            j+=1
        digit_sum-=int(S[N-1-i])*(N-i)
    while not ans[-1]:
        ans.pop()
    print("".join(map(str,reversed(ans))))
if __name__ == "__main__":
    main()