from collections import defaultdict
from collections import deque
from docutils.parsers.rst.directives import path
class Graph:
    def __init__(self):
        self.vertex = defaultdict(list)
        self.nodes =set()
        
    def add_edge(self,start,end=[]):
        self.nodes.add(start)
        if end != []:
            self.nodes.add(end)
            #self.vertex[end].append(start)
            self.vertex[start].append(end)
        else:
           self.vertex[start] = end
        #self.vertex[end].append(start)
        
    def generate_edge(self,dict_edge):
        if dict_edge != None:
            for node in dict_edge:
                for nebr in dict_edge[node]:
                    self.add_edge(node, nebr)
                    
    def bfs(self,start = None):
        visited,to_explore = set(),deque()
        path_tree={}
        travers_list = []
        for start in (self.vertex):
           if start not in visited:
                to_explore.append(start)
                visited.add(start)
                travers_list.append(start)
                while to_explore:
                    next_node = to_explore.popleft()
                    for nxt in self.vertex[next_node]:
                        if nxt not in visited and nxt!=None:
                            visited.add(nxt)
                            travers_list.append(nxt)
                            path_tree[nxt] = next_node
                            to_explore.append(nxt)
        print path_tree
        return travers_list
    
    def find_isolated_nodes(self):
        """ returns a list of isolated nodes. """
        isolated = []
        for node in self.vertex:
            if not self.vertex[node]:
                isolated += node
        return isolated
    def __str__(self):
        res = "Graph:  "
        for node in self.vertex:
            for nebr in self.vertex[node]:
                res += "({}, {})".format(node,nebr)
        return res
    
    def bfs_paths(self,start,end):
        to_explore = deque()
        to_explore.append((start,[start]))
        while to_explore:
            (next_node, path) = to_explore.popleft()
            for nxt in self.vertex[next_node]:
                if nxt not in path:
                    if nxt == end:
                        yield path + [nxt]
                    else:
                        to_explore.append((nxt,path + [nxt]))
    
    def short_path_bfs(self,start,end):
        visited, to_explore = set(),deque()
        visited.add(start)
        to_explore.append(start)
        parent={}
        while to_explore:
            next_node = to_explore.popleft()
            if next_node == end:
                break
            for nxt in self.vertex[next_node]:
                if nxt not in visited:
                    visited.add(nxt)
                    parent[nxt] = next_node
                    to_explore.append(nxt)            
        
        #reconstruct_path
        path = []
        if (end not in visited) or len(parent)==0:
            return path
        else:
            path.append(end)
            current =  parent[end]
            while start != current:
                path.append(current)
                current = parent[current]
            path.append(start)
            
        return path
    def longest_path(self):
        max_diam = 0
        last_vertix = ''
        path = self.bfs()
        if path != None:
            i=len(path)-1
            while i>=0 and path[i] in self.find_isolated_nodes(): 
                i-=1
            last_vertix = path[i]
        for x in self.vertex:
            for path in self.bfs_paths(last_vertix, x):
                max_diam = max(max_diam, len(path))
#         print last_vertix
#         if max_path !=0:        
#             for path in self.bfs(last_vertix):
#                     print path
#                     if max_diam < len(path):
#                         max_diam = len(path)
#             paths = list(self.bfs_paths(x))
#             for y in self.vertex:
#                 if x!=y and x not in self.find_isolated_nodes() and y not in self.find_isolated_nodes():
#                     path = self.short_path_bfs(x,y)
#                     print str(path)+str(x)+str(y)
#                     max_diam = max(max_diam,len(path)-1)
        print max_diam
        
    def diameter(self):
        print "diameter"
        max_diam = 0
        last_vertix = ''
        path = self.bfs()
        paths = []
        if path != None:
            i=len(path)-1
            while i>=0 and path[i] in self.find_isolated_nodes(): 
                i-=1
            last_vertix = path[i]
        for x in self.vertex:
            if x!=last_vertix and x not in self.find_isolated_nodes():
                path = self.short_path_bfs(last_vertix, x)
                print str(path)+str(last_vertix)+str(x)
                if path != None and len(path)!=0:
                    max_diam = max(max_diam, len(path))
        return max_diam
#                     
#         
    def short_path_dfs(self,start,end):
        visited,to_explore = set(), [start]
        visited.add(start)
        parent={}
        while to_explore:
            next_node = to_explore.pop()
            if next_node == end:
                break
            for nxt in self.vertex[next_node]:
                if nxt not in visited:
                    visited.add(nxt)
                    parent[nxt] = next_node
                    to_explore.append(nxt)
        # reconstruct_path
        path = []
        if end not in visited:
            return path
        else:
            path.append(end)
            current =  parent[end]
            while start != current:
                path.append(current)
                current = parent[current]
            path.append(start)
        return path
        
        
    def dfs_paths(self,start,end):
        to_explore = [(start,[start])]
        while to_explore:
            (next_node, path) = to_explore.pop()
            for nxt in self.vertex[next_node]:
                if nxt not in path:
                    if nxt == end:
                        yield path + [nxt]
                    else:
                        to_explore.append((nxt,path + [nxt]))
                    
        
    def dfs(self,start=None):
        visited,to_explore = set(),[start]
        path_tree={}
        travers_list = []
        travers_list.append(start)
        visited.add(start)
        for start in (self.vertex):
            if start not in visited:
                while to_explore:
                     next_node = to_explore.pop()
                     for nxt in self.vertex[next_node]:
                         if nxt not in visited:
                             travers_list.append(nxt)
                             visited.add(nxt)
                             path_tree[nxt] = next_node
                             to_explore.append(nxt)
        print path_tree
        return travers_list
    #reach separate vertex                    
    def dfs_recurvive(self,start):
       visited = set()
       for i in (self.nodes):
           if i not in visited:
               self._dfs_recurvive(i,visited)

    
    def _dfs_recurvive(self,start,visited):
        visited.add(start)
        print start
        for nxt in self.vertex[start]:
                if nxt not in visited:
                    self._dfs_recurvive(nxt,visited)
    #direct graph
    def has_cycle_rec_direct(self):
        visited = set()
        onStack = set()
        for i in self.nodes:
            if i not in visited:
                if self._has_cycle_direct(i,i,visited,onStack) == True:
                    return True
                onStack.remove(i)
        return False
                
    def _has_cycle_direct(self,start,end,visited,onStack):
        visited.add(start)
        onStack.add(start)
        for nxt in self.vertex[start]:
            if nxt not in visited:
                if (nxt not in visited) and(self._has_cycle_direct(nxt,start,visited,onStack) == True):
                    return True
            else:
                if nxt in onStack:
                    return True
        return False
    
    #undirect version O(V+E) 
    def has_cycle_rec(self):
        visited = set()
        for i in self.nodes:
            if i not in visited:
                if self._has_cycle(i,i,visited) == True:    
                    return True
        return False
                
    def _has_cycle(self,start,end,visited):
        visited.add(start)
        for nxt in self.vertex[start]:
            if nxt not in visited:
                if self._has_cycle(nxt,start,visited) == True:
                    return True
            else:
                if nxt != end:
                    return True
        return False
#undirect version O(V+E) #not working
    def has_cycle(self):
        visited = set()
        to_explore = []
        for i in self.vertex:
            if i not in visited:
                to_explore = [(i,i)]
                while to_explore:
                    (node_next,end_node) = to_explore.pop()
                    visited.add(node_next)
                    for nxt in self.vertex[node_next]:
                        if nxt not in visited:
                            to_explore.append((nxt,node_next))
                        else:
                            if nxt != end_node:
                                return True 
        return False
    def topological_sort(self):
        in_degree = [0 for x in self.nodes]
        for i in self.vertex:
            for j in self.vertex[i]:
                in_degree[j] += 1
                
        #in_degree={x:len(y) for x,y in self.vertex.items()}
        queque = deque()
        print in_degree
        for i in self.nodes:
            if in_degree[i]==0:
                queque.append(i)
        
        count = 0
        top_order = []
        while queque:
            node = queque.popleft()
            top_order.append(node)
            
            for i in self.vertex[node]:
                in_degree[i] -=1
                if in_degree[i]==0:
                    queque.append(i)
            count+=1
            
        if count != len(self.nodes):
            print " There is cycle"
        else:
            print top_order
        
class Graph_matrix:
    def __init__(self, V):
        self.vertex=['' for x in range(V)]
        self.size = 0
        self.adj_matrix=[[0 for x in range(V)] for x in range(V) ]
    
    def get_index(self,node_name):
        if node_name in  self.vertex:
            return self.vertex.index(node_name)
        
    def add_edge(self,start,end):
       if start not in  self.vertex:
           self.vertex[self.size] = start
           self.size +=1
       if end not in  self.vertex:
           self.vertex[self.size] = end
           self.size +=1
       self.adj_matrix[self.get_index(start)][self.get_index(end)] = 1
       self.adj_matrix[self.get_index(end)][self.get_index(start)] = 1
    
    def get_neibor(self,node):
        index_node = self.get_index(node)
        for index_neib,x in  enumerate(self.adj_matrix[index_node]):
            if x==1:
                node_neib = self.vertex[index_neib]
                yield  node_neib
    
    def bfs(self,start):
        visited, to_explore = set(),deque()
        for start in (self.vertex):
           if start not in visited:
                to_explore.append(start)
                visited.add(start) 
                while to_explore:
                    cur_node = to_explore.popleft()
                    visited.add(cur_node)
                    print cur_node
                    for nxt in self.get_neibor(cur_node):
                        if nxt not in visited:
                            to_explore.append(nxt)
                            visited.add(nxt)
    
     

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }       
g = Graph()
# g.generate_edge(graph)
# g.add_edge('A','B')
# g.add_edge('A','S')
# g.add_edge('S','G')
# g.add_edge('S','C')
# g.add_edge('G','D')
# g.add_edge('G','E')
# g.add_edge('G','F')
# g.add_edge('C','F')
# g.add_edge('C','H')
# g.add_edge('F','E')

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.nodes.add(6)
print(g.topological_sort())
# print(str(g))
# print(g.bfs('C'))
# print(g.dfs('B'))
# print(g.longest_path())
# print(g.diameter())
# print(g.find_isolated_nodes())
# print(g.short_path_bfs('A', 'H'))
# g.diameter()
# g1 = Graph_matrix(10)
# g1.add_edge('A','B')
# g1.add_edge('A','S')
# g1.add_edge('S','G')
# g1.add_edge('S','C')
# g1.add_edge('G','D')
# g1.add_edge('G','E')
# g1.add_edge('G','F')
# g1.add_edge('C','F')
# g1.add_edge('C','H')
# g1.add_edge('F','E')
# print(g1.bfs('A'))

# # g.add_edge('A','B')
# g.add_edge('A','S')
# g.add_edge('S','G')
# g.add_edge('S','C')
# g.add_edge('G','D')
# g.add_edge('G','E')
# #g.add_edge('F','G')
# g.add_edge('C','F')
# g.add_edge('C','H')
# g.add_edge('H','C')
# #g.add_edge('H','H')
# #g.add_edge('E','F')
# g.add_edge('K','L')

# g.add_edge('A','B')
# g.add_edge('A','S')
# g.add_edge('S','G')
# g.add_edge('S','C')
# g.add_edge('G','D')
# g.add_edge('G','E')
# g.add_edge('G','F')
# g.add_edge('C','F')
# g.add_edge('C','H')
# g.add_edge('F','E')
# g.add_edge('K','L')
# list=[]
# max_len=0
# for v in g.nodes:
#     
#     max_len=max(max_len,len(g.short_path_bfs('A',v)))
# print(max_len)
    
# print("BFS")
# g.bfs("A")
# print("DFS")
# g.dfs("A")
# print("DFS recursive")
# g.dfs_recurvive("A")
# print(list(g.bfs_paths('A','E')))
# print(list(g.dfs_paths('A','E')))
#print(g.short_path_bfs('A', 'E'))
# print(g.short_path_dfs('A', 'E'))
# print(g.has_cycle_rec_direct())
#print(g.has_cycle())
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(3,4)
# g.add_edge(3,5)
# g.add_edge(4,6)
# g.add_edge(4,7)
# g.add_edge(4,8)
# g.add_edge(5,8)
# g.add_edge(5,9)
# g.add_edge(9,7)
# g.add_edge(8,7)
# print(g.BFS(1))

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
