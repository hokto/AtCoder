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
    row = [
        [7],
        [4],
        [2,8],
        [1,5],
        [3,9],
        [6],
        [10]
    ]
    L = len(row)
    S = myin()
    if S[0]=="1":
        print("No")
        return
    isok = False
    for i in range(L):
        f1 = False
        for r in row[i]:
            if S[r-1]=="1": f1 = True
        if not f1: continue
        for j in range(i+1,L):
            f2 = True
            for r in row[j]:
                if S[r-1]=="1": f2 = False
            if not f2: continue
            for k in range(j+1,L):
                f3 = False
                for r in row[k]:
                    if S[r-1]=="1": f3 = True
                if f3: isok = True
    if isok:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()