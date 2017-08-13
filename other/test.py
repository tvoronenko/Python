# def  isSubsetSum(set, n, sum):
#         subset= [[True for x in range(n+1)] for x in range(sum+1)]
#       
#         for i in range(n+1):
#             subset[0][i] = True
#       
#         for i in range(sum+1):
#             subset[i][0] = False
#             
#         for i in range(sum+1):
#             for j in range(n+1):
#                 subset[i][j] = subset[i][j-1]
#                 if (i >= set[j-1]):
#                     subset[i][j] = subset[i][j] or  subset[i - set[j-1]][j-1]
#         for i in range(sum+1):
#             for j in range(n+1):
#                 print(subset[i][j])
#             print("\n")
# 
#         return subset[sum][n]
#     
# print(isSubsetSum([70,30,33,23,4,4,34,95,50,10,10,7],12,108))
from collections import defaultdict
from collections import deque
import math
class Graph:
    def __init__(self):
        self.edge = defaultdict(list)
        self.nodes = {}
        self.cache_path = defaultdict(list)
        self.cache_subtree = defaultdict(list)
        
    def add_edge(self,start,end):
        self.edge[start].append(end)
        self.edge[end].append(start)
    
    def add_node(self,arr):
        self.nodes = {(i+1):v for i,v in enumerate(arr)}
    
    def short_path_bfs(self,start,end):
        visited, to_explore = set(),deque()
        visited.add(start)
        to_explore.append(start)
        parent={}
        while to_explore:
            next_node = to_explore.popleft()
            if next_node == end:
                break
            for nxt in self.edge[next_node]:
                if nxt not in visited:
                    visited.add(nxt)
                    parent[nxt] = next_node
                    to_explore.append(nxt)            
        
        # reconstruct_path
        path = []
        if end not in visited:
            return None
        else:
            path.append(end)
            current =  parent[end]
            while start != current:
                path.append(current)
                current = parent[current]
            path.append(start)
        name_path="{}:{}".format(start,end)
        self.cache_path[name_path]=path
        return path

    def divide(self,param):
        name_path="{}:{}".format(start,end)
        if name_path in self.cache_path:
            path = self.cache_path[name_path]
        else:
            path = self.short_path_bfs(param[0],param[1])
        for i in path:
            self.nodes[i]=math.ceil(self.nodes[i]/param[2])

    def get_subtree(self,node):
        result=[]
        result.append(node)
        to_explore = [node]
        while to_explore:
            current = to_explore.pop()
            for nxt in self.edge[node]:
                if nxt>node:
                    result.append(nxt)
                    to_explore.append(nxt)
        
        self.cache_subtree[node]=result
        return result

    def query(self,param):
        if param[0] in self.cache_subtree:
            subtree = self.cache_subtree[param[0]]
        else:
            subtree = self.get_subtree(param[0])
        max_xor = 0
        for i in subtree:
            max_xor = max(max_xor,(self.nodes[i]^param[1]))
        print(max_xor)

    def multiply(self, param):
        self.nodes[param[0]] = self.nodes[param[0]]*param[1] % 1000 + 9

g=Graph()
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
vertex = list(map(int, input().strip().split(' ')))
g=Graph()
g.add_node(vertex)
for a1 in range(n-1):
        start, end = input().strip().split(' ')
        start, end = [int(start), int(end)]
        g.add_edge(start, end)

for a1 in range(k):
        op = list(map(str, input().strip().split(' ')))
        param = list(map(int,op[1:]))
        if op[0]=="Divide":
            g.divide(param)
        elif op[0]=="Query":
            g.query(param)
        elif op[0]=="Multiply":
            g.multiply(param)