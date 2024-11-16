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
    N = int(myin())
    S = myin()
    cnt = defaultdict(int)
    for i in range(N):
        cnt[S[i]]+=1
    ans = 0
    i = 0
    while i*i<=10**N:
        num = str(i*i).rjust(N,"0")
        #print(num)
        num_cnt = defaultdict(int)
        for k in range(N):
            num_cnt[num[k]]+=1
        flag = True
        for k,v in cnt.items():
            if num_cnt[k]!=v:
                flag = False
        if flag:
            ans+=1        
        i+=1
    print(ans)

if __name__ == "__main__":
    main()