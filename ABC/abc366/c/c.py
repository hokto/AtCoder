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
    Q = int(myin())
    cnt = [0]*(10**6+1)
    ans = 0
    for q in range(Q):
        query = myin_sp_i()
        if query[0]==1:
            x = query[1]
            if cnt[x]==0:
                ans+=1
            cnt[x]+=1
        elif query[0]==2:
            x = query[1]
            if cnt[x]==1:
                ans-=1
            cnt[x]-=1
        else:
            print(ans)
if __name__ == "__main__":
    main()