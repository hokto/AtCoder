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
    from itertools import permutations
    M = int(myin())
    S1 = myin()
    S2 = myin()
    S3 = myin()
    can_digit1 = [False]*10
    for i in range(M):
        can_digit1[int(S1[i])]=True
    can_digit2 = [False]*10
    for i in range(M):
        can_digit2[int(S2[i])]=True
    can_digit3 = [False]*10
    for i in range(M):
        can_digit3[int(S3[i])]=True
    can_digit = []
    for i in range(10):
        can_digit.append(can_digit1[i] and can_digit2[i] and can_digit3[i])
    arr = []
    for i in range(10):
        if can_digit[i]: arr.append(i)
    if not arr:
        print(-1)
        return
    ans = M*3*2
    for v in arr:
        for perm in permutations([S1,S2,S3]):
            res = 0
            now = 0
            for s in perm:
                for _ in range(M):
                    if int(s[now])==v:
                        break
                    res+=1
                    now+=1
                    now%=M
                res+=1
                now+=1
                now%=M
            res-=1
            ans = min(ans,res)
    print(ans)

if __name__ == "__main__":
    main()