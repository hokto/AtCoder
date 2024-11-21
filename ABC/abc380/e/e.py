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
    N,Q = myin_sp_i()
    parent_or_size = [-1]*N
    C = [i for i in range(N)]
    def leader(x):
        if parent_or_size[x]<=0:
            return x
        parent_or_size[x] = leader(parent_or_size[x])
        return parent_or_size[x]
    def merge(u,v):
        u = leader(u)
        v = leader(v)
        if u==v: return
        if u>v: u,v = v,u
        parent_or_size[v] += parent_or_size[u]
        parent_or_size[u] = v
        
    color_size = [1]*N
    for q in range(Q):
        query = myin_sp_i()
        if query[0]==1:
            _,x,c = query
            x-=1
            c-=1
            y = leader(x)
            size = -parent_or_size[y]
            color_size[C[y]]-=size
            C[y]=c
            color_size[C[y]]+=size
            if y-size>=0 and C[leader(y-size)]==c: merge(y-size,y)
            if y+1<N and C[leader(y+1)]==c: merge(y,y+1)
        else:
            _,c = query
            c-=1
            print(color_size[c])

if __name__ == "__main__":
    main()