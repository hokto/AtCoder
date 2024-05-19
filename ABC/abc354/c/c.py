from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

"""
    Implement BinarySearchTree by RedBlackTree.
"""
from typing import Any, List,Union
class BinarySearchTree:
    # color attribute class
    class _RB_Color:
        black = 0
        red = 1
    # include some attribute(parent,left-child,right-child,key,color,subroot-size,subroot-min,subroot-max)
    class _Node:
        def __init__(self,p: Union['_Node']=None,l: Union['_Node']=None,r: Union['_Node']=None,key: Union[Any]=None, color: Union['_RB_Color']=None) -> None:
            self.p: self._Node = p
            self.l: self._Node = l
            self.r: self._Node = r
            self.key: Any = key
            self.color: int = color
            self.size: int = 1
            self.min: Any = key
            self.max: Any = key
    
    def _left_rotate(self,x: _Node) -> None:
        y: self._Node = x.r
        x.r = y.l
        if(y.l!=self._NIL):
            y.l.p = x
        y.p = x.p
        if(x.p == self._NIL):
            self._root = y
        elif(x==x.p.l):
            x.p.l = y
        else:
            x.p.r = y
        y.l = x
        x.p = y
        y.size = x.size
        x.size = x.l.size + x.r.size + 1
        y.min = x.min
        if x.key < x.l.min:
            x.min = x.key
        else:
            x.min = x.l.min
        y.max = x.max
        if x.key > x.r.max:
            x.max = x.key
        else:
            x.max = x.r.max
        
    
    def _right_rotate(self,x: _Node) -> None:
        y: self._Node = x.l
        x.l = y.r
        if(y.r != self._NIL):
            y.r.p = x
        y.p = x.p
        if(x.p==self._NIL):
            self._root = y
        elif(x==x.p.l):
            x.p.l = y
        else:
            x.p.r = y
        y.r = x
        x.p = y
        y.size = x.size
        x.size = x.l.size+x.r.size+1
        y.min = x.min
        if x.key < x.l.min:
            x.min = x.key
        else:
            x.min = x.l.min
        y.max = x.max
        if x.key > x.r.max:
            x.max = x.key
        else:
            x.max = x.r.max
        
    def _insert_fixup(self,z: _Node) -> None:
        while(z.p.color==self._RB_Color.red):
            if(z.p==z.p.p.l):
                y: self._Node = z.p.p.r
                if(y.color == self._RB_Color.red):
                    z.p.p.color = self._RB_Color.red
                    z.p.color = self._RB_Color.black
                    y.color = self._RB_Color.black
                    z = z.p.p
                else:
                    if(z == z.p.r):
                        z = z.p
                        self._left_rotate(z)
                    z.p.color = self._RB_Color.black
                    z.p.p.color = self._RB_Color.red
                    self._right_rotate(z.p.p)
            else:
                y: self._Node = z.p.p.l
                if(y.color == self._RB_Color.red):
                    z.p.p.color = self._RB_Color.red
                    z.p.color = self._RB_Color.black
                    y.color = self._RB_Color.black
                    z = z.p.p
                else:
                    if(z == z.p.l):
                        z = z.p
                        self._right_rotate(z)
                    z.p.color = self._RB_Color.black
                    z.p.p.color = self._RB_Color.red
                    self._left_rotate(z.p.p)
        self._root.color = self._RB_Color.black

    def _delete_at_fixup(self,x: _Node) -> None:
        while(x!=self._root and x.color==self._RB_Color.black):
            if(x.p.l == x):
                w: self._Node = x.p.r
                if(w.color == self._RB_Color.red):
                    w.color = self._RB_Color.black
                    x.p.color = self._RB_Color.red
                    self._left_rotate(x.p)
                    w = x.p.r
                if(w.l.color == self._RB_Color.black and w.r.color == self._RB_Color.black):
                    w.color = self._RB_Color.red
                    x = x.p
                else:
                    if(w.r.color == self._RB_Color.black):
                        w.l.color = self._RB_Color.black
                        w.color = self._RB_Color.red
                        self._right_rotate(w)
                        w = x.p.r
                    w.color = x.p.color
                    x.p.color = self._RB_Color.black
                    w.r.color = self._RB_Color.black
                    self._left_rotate(x.p)
                    x = self._root
            else:
                w: self._Node = x.p.l
                if(w.color == self._RB_Color.red):
                    w.color = self._RB_Color.black
                    x.p.color = self._RB_Color.red
                    self._right_rotate(x.p)
                    w = x.p.l
                    
                if(w.r.color == self._RB_Color.black and w.l.color == self._RB_Color.black):
                    w.color = self._RB_Color.red
                    x = x.p
                else:
                    if(w.l.color == self._RB_Color.black):
                        w.r.color = self._RB_Color.black
                        w.color = self._RB_Color.red
                        self._left_rotate(w)
                        w = x.p.l
                        
                    w.color = x.p.color
                    x.p.color = self._RB_Color.black
                    w.l.color = self._RB_Color.black
                    self._right_rotate(x.p)
                    x = self._root
        x.color = self._RB_Color.black
        
    def _transplant(self,u: _Node,v: _Node) -> None:
        if(u.p == self._NIL):
            self._root = v
        if(u.p.l == u):
            u.p.l = v
        else:
            u.p.r = v
        v.p = u.p
    def __init__(self,max_e: Any=-10**10,min_e: Any=10**10,init_tree:List[Any] = []) -> None:
        self._NIL: self._Node
        self._root: self._Node
        self._inorder_list: List[Any] 
        self._preorder_list: List[Any]
        self._postorder_list: List[Any]
        self._is_init_orders: bool

        self._NIL = self._Node() 
        self._NIL.l = self._NIL
        self._NIL.r = self._NIL
        self._NIL.color = self._RB_Color.black
        self._NIL.size = 0
        self._NIL.min = min_e
        self._NIL.max = max_e
        self._root = self._NIL
        self.init_orders()
        for key in init_tree:
            node = self._Node(key=key)
            self.insert_node(node)
            
    def _min(self,subroot: _Node) -> _Node:
        z: self._Node = subroot
        while(z.l != self._NIL):
            z = z.l
            
        return z
    def min(self) -> Any:
        return self._root.min
    def _max(self,subroot: _Node)  -> _Node:
        z: self._Node = subroot
        while(z.r != self._NIL):
            z = z.r
        return z
    def max(self) -> Any:
        return self._root.max
    
    def insert_node(self,z: _Node) -> None:
        y: self._Node = self._NIL
        x: self._Node = self._root
        while(x!=self._NIL):
            y = x
            y.size += 1
            if y.min > z.key:
                y.min = z.key
            if y.max < z.key:
                y.max = z.key
            if(z.key < x.key):
                x = x.l
            else:
                x = x.r
        z.p = y
        z.l = self._NIL
        z.r = self._NIL
        z.color = self._RB_Color.red
        if(y==self._NIL):
            self._root = z
        elif(y.key > z.key):
            y.l = z
        else:
            y.r = z
        self._insert_fixup(z)

    def insert(self,z: Any) -> None:
        node: self._Node = self._Node(key=z)
        self.insert_node(node)
    def delete_at_node(self,z: _Node) -> None:
        y: self._Node = z
        y_origin_color: self._RB_Color = y.color
        x: self._Node = self._NIL
        w: self._Node  = self._NIL
        if(z.l == self._NIL):
            x = z.r
            self._transplant(z,z.r)
            w = z.r.p
        elif(z.r == self._NIL):
            x = z.l
            self._transplant(z,z.l)
            w = z.l.p
        else:
            y = self._min(z.r)
            y_origin_color = y.color
            x = y.r
            if(y.p == z):
                x.p = y
                w = y
            else:
                w = y.p
                self._transplant(y,y.r)
                y.r = z.r
                y.r.p = y
            self._transplant(z,y)
            y.l = z.l
            y.l.p = y
            y.color = z.color
        while(w!=self._NIL):
            w.size = w.l.size+w.r.size+1
            if w.key < w.l.min:
                w.min = w.key
            else:
                w.min = w.l.min
            if w.key > w.r.max:
                w.max = w.key
            else:
                w.max = w.r.max
            w = w.p
        # fix parameters
        if(y_origin_color == self._RB_Color.black):
            self._delete_at_fixup(x)
    
    def delete(self,key: Any) -> None:
        if(self.is_contain(key)):
            z: self._Node = self.find_node_by_key(key)
            self.delete_at_node(z)
    def init_orders(self) -> None:
        self._preorder_list = []
        self._postorder_list = []
        self._inorder_list = []
        self._is_init_orders = True
    
    def get_inorder(self) -> List[Any]:
        if(not self._is_init_orders):
            return self._inorder_list
        self.solve_orders(self._root)
        self._is_init_orders = False
        return self._inorder_list
    
    def sort(self) -> List[Any]:
        return self.get_inorder()
    
    def get_preorder(self) -> List[Any]:
        if(not self._is_init_orders):
            return self._preorder_list
        self.solve_orders(self._root)
        self._is_init_orders = False
        return self._preorder_list
    
    def get_postorder(self) -> List[Any]:
        if(not self._is_init_orders):
            return self._postorder_list
        self.solve_orders(self._root)
        self._is_init_orders = False
        return self._postorder_list
    
    def solve_orders(self,subroot: _Node) -> None:
        if(subroot == self._NIL): return
        self._preorder_list.append(subroot.key)
        self.solve_orders(subroot.l)
        self._inorder_list.append(subroot.key) 
        self.solve_orders(subroot.r)
        self._postorder_list.append(subroot.key)
        
    def find_node_by_key(self,z: Any) -> _Node:
        x:self._Node = self._root
        while(x!=self._NIL):
            if(x.key == z):
                return x
            elif(x.key > z):
                x = x.l
            else:
                x = x.r
        return self._NIL
    def is_contain(self,z: Any) -> bool:
        node = self.find_node_by_key(z)
        if(node!=self._NIL):
            return True
        else:
            return False
    def is_empty(self) -> bool:
        if(self._root == self._NIL):
            return True
        else:
            return False
    def get_size(self) -> int:
        return self._root.size
    
    def clear(self) -> None:
        self._root = self._NIL
    
    def count(self,key: Any) -> None:
        x: self._Node = self._root
        cnt = 0
        while(x!=self._NIL):
            if(x.key == key):
                cnt+=1
            if(key < x.key):
                x = x.l
            else:
                x = x.r
        return cnt
    def lower_bound(self,key: Any) -> Any:
        y: self._Node = self._NIL
        x: self._Node = self._root
        while(x != self._NIL):
            if(x.key >= key):
                y = x
                x = x.l
            else:
                x = x.r
        return y.key
    def upper_bound(self,key: Any) -> Any:
        y: self._Node = self._NIL
        x: self._Node = self._root
        while(x != self._NIL):
            if(x.key > key):
                y = x
                x = x.l
            else:
                x = x.r
        return y.key
def main():
    N = int(myin())
    AC = []
    bit = BinarySearchTree()
    for i in range(N):
        a,c = myin_sp_i()
        AC.append([a,c,i+1])
        bit.insert(c)
    AC.sort(lambda x: x[0])
    ans = []
    for _,c,i in AC:
        if bit.min()>=c:
            ans.append(i)
        bit.delete(c)
    print(len(ans))
    print(*sorted(ans))

if __name__ == "__main__":
    main()