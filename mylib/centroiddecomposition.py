"""
    Centroid Decomposition
"""
from typing import List,Tuple
class CentroidDecomposition:
    def __init__(self,_tree:List[List[int]],_size:int) -> None:
        self.n:int = _size
        self.tree:List[List[int]] = _tree
        self.parent:List[int] = [-1] * _size
        self.removed:List[int] = [False] * _size
        self.tree_size:List[int] = [0] * _size
        self.depth:List[int] = [0] * _size
        self.centroids:List[int] = []
        self.subtrees:List[Tuple[int,int]] = [] # [(child of centroid,subtree size)]
        
    def find_centroids(self,root:int,size:int) -> None:
        stack:List[Tuple[int,int,int,int]] = [(root,size,-1,0)] # (v,size,p,update) update=0:recursive begin update=1: recursive end
        while stack:
            v,sz,p,update = stack.pop()
            if update == 0:
                self.tree_size[v] = 1
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