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
    A = myin_sp_i()
    S = myin()
    # 逆順で考えて，1桁ならX,2桁ならEX,3桁ならMEXができるように管理
    MS = defaultdict(int)
    for i in range(N)[::-1]:
        if S[i]=="X":
            MS[A[i]+1]+=1
        elif S[i]=="E":
            for k in range(1,3+1):
                if k<=A[i]+1:
                    MS[(A[i]+1)*10+k]+=MS[k]
                else:
                    MS[k*10+(A[i]+1)]+=MS[k]
        else:
            for k1 in range(1,3+1):
                for k2 in range(k1,3+1):
                    if k2<=A[i]+1:
                        MS[(A[i]+1)*100+k2*10+k1]+=MS[k2*10+k1]
                    elif k1<=A[i]+1:
                        MS[k2*100+(A[i]+1)*10+k1]+=MS[k2*10+k1]
                    else:
                        MS[k2*100+k1*10+A[i]+1]+=MS[k2*10+k1]
    #print(MS)
    ans = MS[321]*3+(MS[221]+MS[211])*2+(MS[331]+MS[311]+MS[111])*1
    print(ans)
            

if __name__ == "__main__":
    main()