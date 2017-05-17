from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.vertex = defaultdict(list)
        self.nodes =set()
        
    def add_edge(self,start,end):
        self.vertex[start].append(end)
        self.nodes.add(start)
        self.nodes.add(end)
        #self.vertex[end].append(start)
        
    
    def bfs(self,start):
        visited,to_explore = set(),deque()
        for start in (self.vertex):
           if start not in visited:
                to_explore.append(start)
                visited.add(start)
                while to_explore:
                    next_node = to_explore.popleft()
                    print next_node
                    for nxt in self.vertex[next_node]:
                        if nxt not in visited:
                            visited.add(nxt)
                            to_explore.append(nxt)
    
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
        return path
    
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
                    
        
    def dfs(self,start):
       visited,to_explore = set(),[start]
       while to_explore:
            next_node = to_explore.pop()
            visited.add(next_node)
            print next_node
            for nxt in self.vertex[next_node]:
                if nxt not in visited:
                    to_explore.append(nxt)
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
                  
g = Graph()
# g.add_edge('A','B')
g.add_edge('A','S')
g.add_edge('S','G')
g.add_edge('S','C')
g.add_edge('G','D')
g.add_edge('G','E')
#g.add_edge('F','G')
g.add_edge('C','F')
g.add_edge('C','H')
g.add_edge('H','C')
#g.add_edge('H','H')
#g.add_edge('E','F')
g.add_edge('K','L')

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

# print("BFS")
# g.bfs("A")
# print("DFS")
# g.dfs("A")
# print("DFS recursive")
# g.dfs_recurvive("A")
# print(list(g.bfs_paths('A','E')))
# print(list(g.dfs_paths('A','E')))
# print(g.short_path_bfs('A', 'E'))
# print(g.short_path_dfs('A', 'E'))
print(g.has_cycle_rec_direct())
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
