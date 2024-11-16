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

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def add(self,node:Node):
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def erase(self,node:Node):
        if node.prev == None:
            node.next.prev = None
            self.head = node.next
        elif node.next == None:
            node.prev.next = None
            self.tail = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
    
    def insert(self,node_prev:Node,node_new:Node):
        node_new.prev = node_prev
        node_new.next = node_prev.next
        if node_prev.next != None:
            node_prev.next.prev = node_new
        node_prev.next = node_new
    
    def to_list(self) -> list:
        res = []
        head = self.head
        while head!=None:
            res.append(head.val)
            head = head.next
        return res
        
def main():
    N = int(myin())
    A = myin_sp_i()
    Q = int(myin())
    ll = LinkedList()
    ptr = {}
    for i in range(N):
        node = Node(A[i])
        ptr[A[i]]=node
        ll.add(node)
    for q in range(Q):
        query = myin_sp_i()
        if query[0] == 1:
            x,y = query[1:]
            node_new = Node(y)
            ptr[y]=node_new
            node_prev = ptr[x]
            ll.insert(node_prev,node_new)
        else:
            x = query[1]
            ll.erase(ptr[x])
            ptr[x] = None
    print(*ll.to_list())
            
if __name__ == "__main__":
    main()