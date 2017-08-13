from collections import deque
from _collections import defaultdict
from Queue import PriorityQueue
from heapq import *

class Vertex:
    def __init__(self, data, distance=0, visited = False):
        self.data = data
        self.distance = distance
        self.visited =  visited
                 
    def __hash__(self):
    	return hash(id(self))
 
    def __cmp__(self,other):
        if self.distance < other.distance:
            return -1
        elif self.distance > other.distance:
            return 1
        else:
            return 0
    	    
class Edge:
    def __init__(self, start, end, weight = 0):
        self.start = start
        self.end = end
        self.weight =  weight
        
    def __cmp__(self,other):
        if self.weight < other.weight:
            return -1
        elif self.weight > other.weight:
            return 1
        else:
            return 0
        
    def other(self, vertex):
        if vertex == self.start:
             return self.end
        elif vertex == self.end:
             return self.start

        
class Graph:
    def __init__(self):
        self.vertex = []
        self.adj = defaultdict(list)
    
    def add_edge(self, start,end,weight=0):
        e = Edge(start,end,weight)
        if start not in self.vertex:
            self.vertex.append(start)

        if end != []:
            if end not in self.vertex:
                self.vertex.append(end)
            #self.vertex[end].append(start)
            self.adj[start].append(e)
            #self.adj[end].append(e)
        else:
          self.adj[start] = end
    def edges(self):
        list_edge = []
        for v in self.vertex:
            for e in self.adj[v]:
                if(e.other(v)!=v):
                    yield e
    #a utility function to find set an element i
    #uses path compression technique
    def find(self,parent, i):
        if i in parent and i==parent[i]:
            return i
        return self.find(parent,parent[i])
    
    #a function that does union of two sets of x and y
    #uses union by rank
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        
        #attach smaller rank tree under root of high rank tree
        #union by rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
    #O(ElogE + E log V)        
    def KruskalMST(self):
        result = deque()
        #sort all edge
        q = [] #O(E) space
        #O(ELogE)
        for e in self.edges():
            heappush(q, e)
        
        parent = []
        rank = []
        # Create V subsets with single elements
        for node in self.vertex:
            parent.append(node)
            rank.append(0)
        #we need V-1 edge
        
        while (len(result)<len(self.vertex)-1):
            next_edge = heappop(q)
            x=self.find(parent,next_edge.start)
            y=self.find(parent,next_edge.end)
            #No cycle
            if x!=y:
                result.append(next_edge)
                #O(logV)
                self.union(parent,rank,x,y)
        
        while result:
            e = result.popleft()
            print("Start from {} to {} with weight {}".format(e.start,e.end,e.weight))
    
    def BellmanFord(self,start):
        dist = [float("Inf") for x in self.vertex]
        dist[start] = 0
 
 
        for i in self.vertex:
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for e in self.adj[i]:
                v = e.other(i)
                w = e.weight
                if dist[i] != float("Inf") and dist[i] + w < dist[v]:
                        dist[v] = dist[i] + w
 
        # Step 3: check for negative-weight cycles.  The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.
        for u in self.vertex:
            for e in self.adj[i]:
                v = e.other(i)
                w = e.weight
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print "Graph contains negative weight cycle"
                        return
#         for u, v, w in self.adj:
#                 if dist[u] != float("Inf") and dist[u] + w < dist[v]:
#                         print "Graph contains negative weight cycle"
#                         return
        print dist                 
        # print all distance
        #self.printArr(dist)
            
    def dijkstra(self,start,end):
        visited = set()
        to_explore = []
        heappush(to_explore,(0,start,[]))
        while to_explore:
            (cost,node, path) = heappop(to_explore)
            if node not in visited:
                visited.add(node)
                path = path + [node]
                if node == end:
                    return (cost,path)
                for e in self.adj[node]:
                    nxt = e.other(node)
                    c = e.weight
                    if nxt not in visited:
                        heappush(to_explore,(cost+c,nxt,path))
            
        return (0,[])
        
        
g=Graph()
g.add_edge(0,1, -10)
g.add_edge(0, 2, -6)
g.add_edge(0, 3, -5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, -15)
g.add_edge(4, 5, 3)
g.add_edge(3, 5, 2)
g.BellmanFord(0)
print(g.dijkstra(0,4))