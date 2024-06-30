
"""
    Binary Trie Tree(Lazy ver.)
"""

from typing import List,Union
class BinaryTrie:
    class _Node:
        def __init__(self,prev: Union['_Node']) -> None:
            self.count:int = 0
            self.lazy: int = 0
            self.prev: Union[BinaryTrie._Node] = prev
            self.left: Union[BinaryTrie._Node] = None
            self.right: Union[BinaryTrie._Node] = None
    
    def __init__(self,MAX_DIGIT: int) -> None:
        self.root: BinaryTrie._Node = BinaryTrie._Node(None)
        self.MAX_DIGIT: int = MAX_DIGIT
        self.DIGIT_REV_LIST: List[int] = list(reversed(range(MAX_DIGIT)))
        
    def _eval(self,node: _Node,b: int) -> None:
        if(((node.lazy>>b)&1)>0):
            node.left,node.right = node.right,node.left
        if(node.left):
            node.left.lazy ^= node.lazy
        if(node.right):
            node.right.lazy ^= node.lazy
        node.lazy = 0
    
    def get_count(self,node: Union[_Node]) -> int:
        return node.count if node else 0
    def insert(self,val: int,size:int = 1) -> None:
        node: BinaryTrie._Node = self.root
        for i in self.DIGIT_REV_LIST:
            node.count += size
            self._eval(node=node,b=i)
            b: int = (val>>i)&1
            if(b > 0 and not node.right):
                node.right = BinaryTrie._Node(node)
            if(b==0 and not node.left):
                node.left = BinaryTrie._Node(node)
            if(b>0):
                node = node.right
            else:
                node = node.left
        node.count += size
    def clear(self,node: _Node) -> Union[_Node]:
        if(not node or self.get_count(node=node)>0):
            return node
        #del node
        return None
    
    def delete_node(self, node: _Node,size: int = 1) -> bool:
        if(not node):
            return False
        while(node.prev):
            node.count -= size
            node = node.prev
            node.left = self.clear(node.left)
            node.right = self.clear(node.right)
        node.count -= 1
        return True 
    
    def find(self,val: int) -> Union[_Node]:
        node: BinaryTrie._Node = self.root
        for i in self.DIGIT_REV_LIST:
            self._eval(node=node,b=i)
            b: int = (val>>i)&1
            if(b > 0):
                node = node.right
            else:
                node = node.left
            if(not node):
                return node
        return node
    
    def delete(self,val: int,size:int = 1) -> bool:
        node: Union[BinaryTrie._Node] = self.find(val=val)
        return self.delete_node(node=node,size=size)
    
    def get(self,node: _Node) -> int:
        if(not node):
            return -1
        val: int = 0
        for i in range(self.MAX_DIGIT):
            if(node == node.prev.right):
                val |= (1<<i)
            node = node.prev
        return val
                
    def get_min(self,bias: int = 0) -> _Node:
        node: Union[BinaryTrie._Node] = self.root
        for i in self.DIGIT_REV_LIST:
            self._eval(node=node,b=i)
            b: int = (bias >> i)&1
            if(not node.left):
                node = node.right
            elif(not node.right):
                node = node.left
            elif(b > 0):
                node = node.right
            else:
                node = node.left
        return node
    
    def min_element(self,bias = 0) -> int:
        return self.get(self.get_min(bias=bias))
    
    def max_element(self,bias=0) -> int:
        return self.get(self.get_min(bias=~bias))
    # 0-indexed 
    def get_kth_node(self,k:int) -> _Node:
        node: Union[BinaryTrie._Node] = self.root
        if(self.get_count(node)<=k):
            return None
        for i in self.DIGIT_REV_LIST:
            self._eval(node=node,b=i)
            if(self.get_count(node.left)<=k):
                k-= self.get_count(node.left)
                node = node.right
            else:
                node = node.left
        return node
   
    def kth_element(self,k:int) -> int:
        return self.get(self.get_kth_node(k=k))
    
    def get_current_node(self,node: _Node,b:int)  -> _Node:
        while(node):
            if(b<0):
                break
            self._eval(node=node,b=b)
            if(node.left):
                node = node.left
            elif(node.right):
                node = node.right
            b-=1
        return node
    
    def get_next_node(self,node: _Node,b: int) -> _Node:
        while(node.prev):
            if(node == node.prev.left and node.prev.right):
                return self.get_current_node(node=node,b=b)
            node = node.prev
            b+=1
        return node
                
    def lower_bound_node(self,val: int) -> _Node:
        node: BinaryTrie._Node = self.root
        for i in self.DIGIT_REV_LIST:
            self._eval(node=node,b=i)
            b: int = (val>>i)&1
            if(b>0 and node.right):
                node = node.right
            elif(b==0 and node.left):
                node = node.left
            elif(b>0):
                return self.get_next_node(node=node,b=i)
            else:
                return self.get_current_node(node=node,b=i)
        return node
    
    def upper_bound_node(self,val:int) -> _Node:
        return self.lower_bound(val+1)
    
    def lower_bound(self,val: int) -> int:
        return self.get(self.lower_bound_node(val=val))
    
    def upper_bound(self,val: int) -> int:
        return self.get(self.upper_bound_node(val=val))
    
    def xor_all(self,val: int) -> None:
        if(self.root):
            self.root.lazy ^= val
            
    def __getitem__(self,position: int) -> int:
        return self.kth_element(k=position)
L,Q = list(map(int,input().split()))
bt = BinaryTrie(30)
bt.insert(L)
for q in range(Q):
    c,x = list(map(int,input().split()))
    if c==1:
        bt.insert(x)
    else:
        l = bt.lower_bound(x)
        r_idx = bt.get_count(bt.find(l))
        r = bt[r_idx]
        print(f"l:{l}")
        print(f"r:{r}")
        print(r-l)