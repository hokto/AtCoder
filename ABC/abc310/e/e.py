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
    one_cnt = [0]*N
    if S[0]=="1": one_cnt[0]=1
    for i in range(1,N):
        if S[i]=="1":
            one_cnt[i]+=i+1-one_cnt[i-1]
        else:
            one_cnt[i]=i
    print(sum(one_cnt))

if __name__ == "__main__":
    main()