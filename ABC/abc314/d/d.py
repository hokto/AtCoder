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
    S = list(myin())
    Q = int(myin())
    query = []
    for q in range(Q):
        query.append(myin_sp_s())
    all_change_idx = -1
    for q in range(Q)[::-1]:
        if query[q][0]!="1":
            all_change_idx = q
            break
    for q in range(Q):
        if q == all_change_idx:
            if query[q][0]=="2":
                for i in range(N):
                    S[i] = S[i].lower()
            else:
                for i in range(N):
                    S[i] = S[i].upper()
        else:
            if query[q][0]=="1":
                S[int(query[q][1])-1]=query[q][2]
    print("".join(S))

if __name__ == "__main__":
    main()