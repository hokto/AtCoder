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
    K = int(myin())
    S = myin()
    T = myin()
    if len(S)==len(T):
        diff = 0
        for i in range(len(S)):
            if S[i]!=T[i]: diff+=1
        if diff<=1:
            print("Yes")
        else:
            print("No")
    else:
        if len(S)>len(T): S,T = T,S
        if len(S)+1==len(T):
            same_cnt_l = 0
            for i in range(len(S)):
                if S[i]!=T[i]:
                    break
                same_cnt_l +=1
            same_cnt_r = 0
            for i in range(len(S))[::-1]:
                if S[i]!=T[i+1]:
                    break
                same_cnt_r +=1
            if same_cnt_l+same_cnt_r>=len(S):
                print("Yes")
            else:
                print("No")
        else:
            print("No")

if __name__ == "__main__":
    main()