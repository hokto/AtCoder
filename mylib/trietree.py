"""
    Implement TrieTree
"""
from typing import List
class TrieTree:
    # TrieTree's node structure
    class _TrieNode:
        def __init__(self,dist,char_size:int) -> None:
            self.next: List[int] = [-1 for _ in range(char_size)]
            self.common: int = 0 
            self.accept: List[int] = []
            self.dist: int = dist
            
    def __init__(self,char_size: int,base: str) -> None:
        self.char_size: int = char_size
        self.base:str = base
        self.base_ord: int = ord(base)
        self.nodes: List[TrieTree._TrieNode] = []
        self.root = 0
        self.nodes.append(TrieTree._TrieNode(dist=self.root,char_size=self.char_size))
    
    def add_direct(self,word: str, word_id: int) -> None:
        node_id: int = 0
        for i in range(len(word)):
            dist:int = ord(word[i])-self.base_ord
            next_id:int = self.nodes[node_id].next[dist]
            if(next_id == -1):
                next_id = len(self.nodes)
                self.nodes[node_id].next[dist] = next_id
                self.nodes.append(TrieTree._TrieNode(dist=dist,char_size=self.char_size))
            self.nodes[node_id].common += 1
            node_id = next_id
        self.nodes[node_id].common += 1
        self.nodes[node_id].accept.append(word_id)
    
    def add(self,word: str) -> None:
        self.add_direct(word,self.nodes[0].common)
    
    def search(self,word: str, prefix:bool = False) -> bool:
        node_id: int = 0
        for i in range(len(word)):
            dist:int = ord(word[i]) - self.base_ord
            next_id:int = self.nodes[node_id].next[dist]
            if(next_id == -1):
                return False
            node_id = next_id
        return (True if prefix else len(self.nodes[node_id].accept)>0)
    
    def start_with(self,word:str) -> bool:
        return self.search(word=word,prefix=True)
    
    def count(self) -> int:
        return self.nodes[0].common
    
    def size(self) -> int:
        return len(self.nodes)