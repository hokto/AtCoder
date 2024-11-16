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
    S = myin()
    T = myin()
    ATCODER = list("atcoder")
    S_at_cnt = S.count("@")
    T_at_cnt = T.count("@")
    S_ab_cnt = defaultdict(int)
    T_ab_cnt = defaultdict(int)
    L = len(S)
    for i in range(L):
        if S[i]!="@": S_ab_cnt[S[i]]+=1
        if T[i]!="@": T_ab_cnt[T[i]]+=1
    INF = L+1
    S_diff_cnt = 0
    T_diff_cnt = 0
    AB = [chr(ord("a")+i) for i in range(26)]
    for k in AB:
        v = S_ab_cnt[k]
        if T_ab_cnt[k]>v:
            if k in ATCODER:
                S_diff_cnt+=T_ab_cnt[k]-v
            else:
                S_diff_cnt+=INF
    for k in AB:
        v = T_ab_cnt[k]
        if S_ab_cnt[k]>v:
            if k in ATCODER:
                T_diff_cnt+=S_ab_cnt[k]-v
            else:
                T_diff_cnt+=INF
    if S_diff_cnt<=S_at_cnt and T_diff_cnt<=T_at_cnt:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()