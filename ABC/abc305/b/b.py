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
    P,Q = myin_sp_s()
    if P>Q: P,Q = Q,P
    dist = [0,3,4,8,9,14,23]
    print(dist[ord(Q)-ord("A")]-dist[ord(P)-ord("A")])

if __name__ == "__main__":
    main()