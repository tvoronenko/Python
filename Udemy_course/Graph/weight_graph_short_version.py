from collections import defaultdict
from collections import deque
class Vertex:
    def __init__(self,name):
        self.name = name
        
    def __hash__(self):
        return hash(id(self))
    
class Edge:
    def __init__(self,start,end,weight=0):
        self.start = start
        self.end = end
        self.weight = weight
        
    def __hash__(self):
        return hash((self.start,self.end))
class Graph:
    def __init__(self):
        self.vertex = defaultdict(list)
        self.nodes =set()
    
    def add_edge(self,start,end,weight):
        if len(self.vertex[start])==0:
            self.vertex[start]=defaultdict(list)
        self.vertex[start][end]=weight
        self.nodes.add(start)
        self.nodes.add(end)