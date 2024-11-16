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
    A= myin_sp_i()
    indices = [[] for i in range(N)]
    ans = 0
    for i,a in enumerate(A):
        a-=1
        indices[a].append(i)
    for i in range(N):
        for j in range(len(indices[i])):
            if j==0:
                if j==len(indices[i])-1:
                    ans+=(N-indices[i][j])*(indices[i][j]+1)
                else:
                    ans+=(indices[i][j+1]-indices[i][j])*(indices[i][j]+1)
            elif j==len(indices[i])-1:
                ans+=(N-indices[i][j])*(indices[i][j]+1)
            else:
                ans+=(indices[i][j+1]-indices[i][j])*(indices[i][j]+1)
    print(ans)

if __name__ == "__main__":
    main()