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
    T = int(myin())
    for t in range(T):
        K = int(myin())
        # 9進数に変換
        res = []
        while K:
            if K%9==0:
                res.append(9)
                K//=9
                K-=1
            else:
                res.append(K%9)
                K//=9
        ans = []
        prev = 0
        for v in res[::-1]:
            if v>=prev:
                ans.append(str(v))
            else:
                ans.append(str(v-1))
            prev = v
        print("".join(ans))

if __name__ == "__main__":
    main()