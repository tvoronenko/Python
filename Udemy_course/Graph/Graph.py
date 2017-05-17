class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def dfs_rec(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs_rec(graph, nxt, visited)
    return visited

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))
                
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

                       
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# g.addEdge(7,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
 
graph = {'A': set(['B', 'S']),
         'B':set([]),
         'S': set(['G', 'C']),
         'C': set(['H', 'F']),
         'G': set(['D','E','F']),
         'H': set(['E']),
         'E':set([]),
         'D':set([]),
         'F': set(['E'])}
print(dfs(graph, 'A'))
print(dfs_rec(graph, 'A'))
print(list(dfs_paths(graph, 'A', 'F')))
print(bfs(graph, 'A') )
print(list(bfs_paths(graph, 'A', 'F')))
print(shortest_path(graph, 'A', 'F'))
# d = {}
# g = Graph()
# 
# wfile = open('words.txt','r')
# # create buckets of words that differ by one letter
# for line in wfile:
#     print line
#     word = line[:-1]
#     print word
#     for i in range(len(word)):
#         bucket = word[:i] + '_' + word[i+1:]
#         if bucket in d:
#             d[bucket].append(word)
#         else:
#             d[bucket] = [word]
# # add vertices and edges for words in the same bucket
# for bucket in d.keys():
#     for word1 in d[bucket]:
#         for word2 in d[bucket]:
#             if word1 != word2:
#                 g.addEdge(word1,word2)
# 
# print(g)
