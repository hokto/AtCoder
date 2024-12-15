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
    P = myin_sp_i()
    S = ["A","B","C","D","E"]
    ans = []
    N = 5
    for bit in range(1,1<<N):
        res = []
        p = 0
        for i in range(N):
            if bit&(1<<i):
                res.append(S[i])
                p+=P[i]
        ans.append((p,"".join(res)))
    ans.sort(lambda x:(-x[0],x[1]))
    for _,name in ans:
        print(name)
if __name__ == "__main__":
    main()