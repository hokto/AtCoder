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
    P = myin_sp_i()
    prev = N+1
    B = []
    for i in range(N)[::-1]:
        if prev<P[i]:
            B.append(P[i])
            B.sort()
            idx = B.index(P[i])-1
            C = []
            for k in range(i):
                C.append(P[k])
            C.append(B[idx])
            B.remove(B[idx])
            C+=reversed(B)
            print(*C)
            break
        else:
            prev = P[i]
            B.append(P[i])
if __name__ == "__main__":
    main()