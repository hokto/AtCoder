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
    N = int(myin())
    R = myin()
    C = myin()
    A = ["A","B","C"] + ["."]*(N-3)
    ans = []
    def solve(i,S):
        nonlocal ans
        if i==N:
            for j in range(N):
                f = False
                row = []
                for k in range(N):
                    if S[k][j]==".": continue
                    row.append(S[k][j])
                if not(len(row)>0 and row[0]==C[j] and ("A" in row and "B" in row and "C" in row)):
                    return
            ans = [[S[k][j] for j in range(N)]for k in range(N)]
            return
        hash = set()
        for perm in permutations(A):
            f = True
            for j in range(N):
                if perm[j]==".": continue
                if perm[j]!=R[i]: f=False
                break
            if not f: continue
            s = "".join(perm)
            if s in hash:
                continue
            hash.add(s)
            for j in range(N):
                S[i][j] = perm[j]
            solve(i+1,S)
    solve(0,[[""]*N for _ in range(N)])
    if ans:
        print("Yes")
        for a in ans:
            print("".join(a))
    else:
        print("No")
            
if __name__ == "__main__":
    main()