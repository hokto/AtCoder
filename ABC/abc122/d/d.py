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
    # 禁止事項:
    # AGCがこの順で部分列として含まれる
    # A?CGがこの順で部分列として含まれる
    # GA?Cがこの順で部分列として含まれる
    # dp[i][j]:=i番目までで文字jを選んだ時に条件を満たす文字列の数
    MOD = 10**9+7
    N = int(myin())
    dp = [defaultdict(int) for _ in range(N+1)]
    dp[0]["TTT"] = 1
    for i in range(N):
        for s in dp[i].keys():
            for c in ["T","A","G","C"]:
                t = s+c # 4文字にする
                isok = True
                for k in range(4):
                    if k>=1:
                        tt = list(t)
                        tt[k-1],tt[k]=tt[k],tt[k-1]
                        if "".join(tt).count("AGC")>0:
                            isok = False
                    if t.count("AGC")>0:
                        isok = False
                if isok:
                    dp[i+1][t[1:]]+=dp[i][s]
                    dp[i+1][t[1:]]%=MOD
    ans = 0
    for v in dp[-1].values():
        ans+=v
        ans%=MOD
    print(ans)

if __name__ == "__main__":
    main()