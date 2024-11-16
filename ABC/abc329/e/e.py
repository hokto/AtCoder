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
    N,M = myin_sp_i()
    S = list(myin())
    T = list(myin())
    que = []
    used = [False]*N
    for i in range(N-M+1):
        if S[i:i+M]==T[:]:
            que.append(i)
    while que:
        i = que.pop()
        if used[i]: continue
        used[i] = True
        for j in range(M):
            S[i+j]="#"
        for j in range(-M+1,M):
            if 0<=i+j and i+j+M-1<N and not used[i+j]:
                flag = True
                for k in range(M):
                    if not(S[i+j+k]=="#" or S[i+j+k]==T[k]):
                        flag = False
                if flag:
                    que.append(i+j)
    #print(S)
    ans = True
    for i in range(N):
        if S[i]!="#":
            ans = False
    print("Yes" if ans else "No")
if __name__ == "__main__":
    main()