from collections import deque

class Vertex:
    def __init__(self, data, distance=0, visited = False):
        self.data = data
        self.distance = distance
        self.out_degree =  {}
        self.visited =  visited
    
    def add_edge(self,edge):
         self.out_degree[edge.end] = edge
         
    def __str__(self):
        if len(self.out_degree) == 0:
             return str(self.data) + ' connectedTo: []'
        return str(self.data) + ' connectedTo: ' + str([x.data for x in self.out_degree])
         
         
class Edge:
    def __init__(self, start, end, weight = 0):
        self.start = start
        self.end = end
        self.weight =  weight
        
        
class Graph:
    def __init__(self):
        self.edges = []
        self.vertex = []
    
    def add_edge(self, start_data,end_data,weight=0):
        if start_data == None or end_data == None:
            raise ValueError("Null data")
        start = self.get_first_vertex_with_data(start_data)
        end = self.get_first_vertex_with_data(end_data)
        if  start is None:
            start = Vertex(start_data)
            self.vertex.append(start)
        if  end is None:
            end = Vertex(end_data)
            self.vertex.append(end)
        new_edge = Edge(start,end,weight)
        self.edges.append(new_edge)
        start.add_edge(new_edge)
    
    def do_all_node_unvisited(self):
        for node in self.vertex:
            node.visited = False
    
    def __str__(self):
        for node in self.vertex:
            if node is not None:
                print(str(node))
    #get first vertex with data if it in graph
    def get_first_vertex_with_data(self, data):
        for vertex in self.vertex:
            if vertex.data == data:
                return vertex
        return None
             
    def bfs(self,start_data, end_data):
        if start_data is None or end_data is None:
            raise ValueError("Cannot find route from or to null node")
        start = self.get_first_vertex_with_data(start_data)
        end = self.get_first_vertex_with_data(end_data)
        if start is None or end is None:
            raise ValueError("Cannot find route from or to in Graph") 
        self.do_all_node_unvisited()
        parentMap={}
        found = self._bfs(start, end,parentMap);
        if not found:
            print("No path found from " + start_data+ " to " + end_data)
            return None
        # reconstruct the path
        path = self._reconstructPath(start, end,parentMap);

        return path;
    
    def dfs(self,start_data, end_data):
        if start_data is None or end_data is None:
            raise ValueError("Cannot find route from or to null node")
        start = self.get_first_vertex_with_data(start_data)
        end = self.get_first_vertex_with_data(end_data)
        if start is None or end is None:
            raise ValueError("Cannot find route from or to in Graph") 
        self.do_all_node_unvisited()
        parentMap={}
        found = self._dfs(start, end,parentMap);
        if not found:
            print("No path found from " + start_data+ " to " + end_data)
            return None
        # reconstruct the path
        path = self._reconstructPath(start, end,parentMap);

        return path;
        
    def _reconstructPath(self,start, end,parentMap ):
        if end.visited == False:
            return None
        path = []
        current = end
        while current.data != start.data:
            path.append(current.data)
            current = parentMap[current]
        path.append(start.data)
        return path;
    
    def _bfs(self,start, end,parentMap):
        to_explore = deque()
        to_explore.append(start)
        start.visited = True
        found = False
        
        while(len(to_explore) != 0):
            next_node = to_explore.popleft()
            
            if next_node.data == end.data:
                found = True
                break
            
            for neibr in next_node.out_degree:
                if  neibr.visited == False:
                    neibr.visited = True
                    parentMap[neibr] = next_node
                    to_explore.append(neibr)
        return found
    
    def _dfs(self,start, end,parentMap):
        to_explore = []
        to_explore.append(start)
        start.visited = True
        found = False
        
        while(len(to_explore) != 0):
            next_node = to_explore.pop()
            
            if next_node.data == end.data:
                found = True
                break
            
            for neibr in next_node.out_degree:
                if  neibr.visited == False:
                    neibr.visited = True
                    parentMap[neibr] = next_node
                    to_explore.append(neibr)
        return found
    
    def dfs_all_path(self,start,end):
        start_n= self.get_first_vertex_with_data(start)
        stack = [(start_n, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for nxt in vertex.out_degree:
                if nxt.data in nxt.data:
                    if nxt.data == end:
                        yield path + [nxt.data]
                    else:
                        stack.append((nxt, path + [nxt.data]))
#     def _dfs_recurs(self,start, end,parentMap):
#         start.visited = True
#         found = False
#         if start.data == end.data:
#             return True
#             
#         for neibr in start.out_degree:
#             if  neibr.visited == False:
#                 found = _dfs_recurs(neibr, end,parentMap)
#         return found
    
g=Graph()
g.add_edge('A','B')
g.add_edge('A','S')
g.add_edge('S','G')
g.add_edge('S','C')
g.add_edge('G','D')
g.add_edge('G','E')
g.add_edge('G','F')
g.add_edge('C','F')
g.add_edge('C','H')
g.add_edge('H','E')
g.add_edge('F','E')
print(g.__str__())
print(g.bfs('A','E'))
print(g.dfs('A','E'))
print(list(g.dfs_all_path('A','E')))

