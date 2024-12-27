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
    from bisect import bisect_left,bisect_right
    N,M,Sx,Sy = myin_sp_i()
    X = defaultdict(list)
    Y = defaultdict(list)
    for i in range(N):
        x,y = myin_sp_i()
        X[x].append((y,i))
        Y[y].append((x,i))
    arrival_cnt_X = defaultdict(list)
    arrival_cnt_Y = defaultdict(list)
    for x in X.keys():
        X[x].sort()
        arrival_cnt_X[x] = [0]*(len(X[x])+1)
    for y in Y.keys():
        Y[y].sort()
        arrival_cnt_Y[y] = [0]*(len(Y[y])+1)
    for _ in range(M):
        d,c = myin_sp_s()
        c = int(c)
        if d=="U":
            if Sx in X: 
                l = bisect_left(X[Sx],Sy,key=lambda x: x[0])
                r = bisect_right(X[Sx],Sy+c,key=lambda x:x[0])
                arrival_cnt_X[Sx][l]+=1
                arrival_cnt_X[Sx][r]-=1
            Sy+=c
        elif d=="D":
            if Sx in X:
                l = bisect_left(X[Sx],Sy-c,key=lambda x:x[0])
                r = bisect_right(X[Sx],Sy,key=lambda x:x[0])
                arrival_cnt_X[Sx][l]+=1
                arrival_cnt_X[Sx][r]-=1
            Sy-=c
        elif d=="L":
            if Sy in Y:
                l = bisect_left(Y[Sy],Sx-c,key=lambda x:x[0])
                r = bisect_right(Y[Sy],Sx,key=lambda x:x[0])
                arrival_cnt_Y[Sy][l]+=1
                arrival_cnt_Y[Sy][r]-=1
            Sx-=c
        else:
            if Sy in Y:
                l = bisect_left(Y[Sy],Sx,key=lambda x:x[0])
                r = bisect_right(Y[Sy],Sx+c,key=lambda x:x[0])
                arrival_cnt_Y[Sy][l]+=1
                arrival_cnt_Y[Sy][r]-=1
            Sx+=c
    is_arrival = [False]*N
    for x,arr in arrival_cnt_X.items():
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s>0:
                is_arrival[X[x][i][1]] = True
    for y,arr in arrival_cnt_Y.items():
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s>0:
                is_arrival[Y[y][i][1]] = True
    print(Sx,Sy,sum(is_arrival))

if __name__ == "__main__":
    main()