from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    H,W = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    row = [0 for i in range(H)]
    col = [0 for i in range(W)]
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                row[i]+=1
                col[j]+=1
    print(f"{row.index(max(row)-1)+1} {col.index(max(col)-1)+1}")
if __name__ == "__main__":
    main()