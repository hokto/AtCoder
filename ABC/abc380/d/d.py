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
    # 反転:1,2,4,7,8,11,13,14
    # 通常:0,3,5,6,9,10,12,15
    S = myin()
    L = len(S)
    Q = int(myin())
    K = myin_sp_i()
    ans = []
    for k in K:
        s = (k-1)//L
        r = (k-1)%L
        if s.bit_count()&1:
            ans.append(S[r].swapcase())
        else:
            ans.append(S[r])
    print(*ans)
if __name__ == "__main__":
    main()