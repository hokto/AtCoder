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
    Q = int(myin())
    MAX_M = 2*10**5+1
    box = [[] for i in range(N+1)]
    card = [set() for i in range(MAX_M)]
    for q in range(Q):
        query = myin_sp_i()
        if query[0]==1:
            i = query[1]
            j = query[2]
            box[j].append(i)
            card[i].add(j)
        elif query[0]==2:
            i = query[1]
            print(*sorted(box[i]))
        else:
            i = query[1]
            print(*sorted(card[i]))
if __name__ == "__main__":
    main()