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
    from atcoder.fenwicktree import FenwickTree
    # 全体でi番目の要素が集合A_idxにあることがわかって，かつA_idxの中でj番目であることがわかれば，
    # idx~N-1までの集合に対して，j番目以上になり，どれほどその番数が上がるかどうかは結局合計して残りの分だけになる．
    # 今，i番目でしかもA_idxにはすでにj個あることがわかっているため，残りはi-jであることがわかる．
    # よって，答えに寄与する値は(N-1-idx)*(j+1)+i-jと計算できる(ただし，i,jは0-indexed)
    N,M = myin_sp_i()
    A = []
    B = []
    for _ in range(N):
        A.append(myin_sp_i())
        for a in A[-1]:
            B.append(a)
    change = {}
    for i,b in enumerate(sorted(B)):
        change[b] = i
    idx_of_set = [-1]*(N*M) # idx_of_set[a]=iならA[i]にaが含まれている
    for i in range(N):
        for j in range(M):
            A[i][j] = change[A[i][j]]
            idx_of_set[A[i][j]] = i
    ft = FenwickTree(N)
    ans = 0
    for i in range(N*M):
        idx = idx_of_set[i]
        resi = i-ft.sum(0,idx+1)
        ans+=resi+(ft.sum(idx,idx+1)+1)*(N-1-idx)
        #print(i,":",resi+(ft.sum(idx,idx+1)+1)*(N-1-idx))
        ft.add(idx,1)
    print(ans)
    

if __name__ == "__main__":
    main()