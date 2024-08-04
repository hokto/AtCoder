from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
"""
    Centroid Decomposition
"""
from typing import List,Tuple
class CentroidDecompositionEx:
    def __init__(self,_tree:List[List[int]],_size:int,_weight:List[int]) -> None:
        self.n:int = _size
        self.tree:List[List[int]] = _tree
        self.parent:List[int] = [-1 for _ in range(_size)]
        self.removed:List[int] = [False for _ in range(_size)]
        self.tree_size:List[int] = [0 for _ in range(_size)]
        self.depth:List[int] = [0 for _ in range(_size)]
        self.centroids:List[int] = []
        self.subtrees:List[Tuple[int,int]] = [] # [(child of centroid,subtree size)]
        self.weight:List[int] = _weight
        self.sum_weight:int = sum(_weight)
        
    def find_centroids(self,root:int,size:int) -> None:
        stack:List[Tuple[int,int,int,int]] = [(root,size,-1,0)] # (v,size,p,update) update=0:recursive begin update=1: recursive end
        while stack:
            v,sz,p,update = stack.pop()
            if update == 0:
                self.tree_size[v] = self.weight[v]
                self.parent[v] = p
                stack.append((v,sz,p,1))
                for ch in self.tree[v]:
                    if(ch == p): continue
                    if(self.removed[ch]): continue
                    stack.append((ch,sz,v,0))
            else:
                is_centroid = True
                for ch in self.tree[v]:
                    if(ch == p): continue
                    if(self.removed[ch]): continue
                    if(self.tree_size[ch] > sz/2):
                        is_centroid = False
                    self.tree_size[v] += self.tree_size[ch]
                if(sz - self.tree_size[v] > sz/2):
                    is_centroid = False
                if(is_centroid):
                    self.centroids.append(v)
    def get_centroid(self,root:int,size) -> int:
        self.centroids = []
        self.find_centroids(root=root,size=size)
        return self.centroids[0]
    def build(self,root:int,size:int) -> None:
        stack:List[Tuple[int,int,int,int,int]] = [(root,size,-1,0,0)] # (v,size,prev_centroid,d,update)
        while stack:
            v,sz,prev_centroid,d,update = stack.pop()
            if update == 0:
                centroid = self.get_centroid(root=v,size=sz)
                self.removed[centroid] = True
                self.depth[centroid] = d
                stack.append((v,sz,centroid,d,1))
                for ch in self.tree[centroid]:
                    if(self.removed[ch]): continue
                    if(ch == self.parent[centroid]):
                        stack.append((ch,sz-self.tree_size[centroid],-1,d+1,0))
                    else:
                        stack.append((ch,self.tree_size[ch],-1,d+1,0))
            else:
                self.removed[prev_centroid] = False
def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def solve(v,p,G,C,d):
    res = C[v]*d
    for vv in G[v]:
        if(vv==p): continue
        res+=solve(vv,v,G,C,d+1)
    return res
def main():
    N = int(myin())
    G = [[] for i in range(N)]
    for i in range(N-1):
        A,B = myin_sp_i()
        A-=1
        B-=1
        G[A].append(B)
        G[B].append(A)
    C = myin_sp_i()
    cd = CentroidDecompositionEx(G,N,C)
    centroid = cd.get_centroid(0,cd.sum_weight)
    print(solve(centroid,-1,G,C,0))

if __name__ == "__main__":
    main()