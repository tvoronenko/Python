from pylint.pyreverse.vcgutils import GRAPH_ATTRS
class Vertex:
    def __init__(self,x):
        self._element = x
        
    def element(self):
        return self._element
    
    def __hash__(self):
        """Will allow vertex to be a map/set key"""
        return hash(id(self))

class Edge:
    def __init__(self,u,v,x):
        self._origin = u
        self._destination = v
        self._element = x
    
    def endpoints(self):
        """"Return (u,v) tuple for vertices u and v"""
        return (self._origin, self._destination)
    
    def opposite(self,v):
        """Return the vertex that is opposite v on this edge"""
        return self._destination if v is self._origin else self._destination
    
    def element(self):
        return self._element
    
    def __hash__(self):
        """Will allow vertex to be a map/set key"""
        return hash((self._origin, self._destination))
    
    class Graph:
        """Using adjacency map"""
        
        def __init__(self, directed = False):
            """Create an empty graph(undirect, by default
            Graph is directed if optional parameter is set to True
            """
            self.outgoing = {}
            #only create second map for directed graph
            self._incoming = {} if directed else self._outgoing
            
        def is_directed(self):
            """Return True if this is directed graph; False if undirected
            Property is based on the original declaration of the graph,
            not its content
            """
            return self._incoming is not self._outgoing # directed if map distinct
        
        def vertex_count(self):
            return len(self._outgoing)
        
        def vertices(self):
            return self._outgoing.keys()
        
        def edge_count(self):
            total = sum(len(self._outgoing[v]) for v in self._outgoing)
            #for i=undirected grapsh make sure not to double-count EDGE_ATTRS
            return total if self.is_directed() else total //2
        
        def edges(self):
            result= set()
            #avoid double-reporting edges of undirected graph
            for secondary_map in self._outgoing.values():
                result.update(secondary_map)
            return result
        
        def get_edge(self,u,v):
            return self._outgoing[u].get(v)
        
        def degree(self,v,outgoing = True):
            """Return number of (outgoing) edges incedent to vertex v in the Graph
            If graph is directed, optional parameters is used to count incoming edges
            """
            adj = self._outgoing if outgoing else self._incoming
            return len(adj[v])
        
        def incident_edges(self,v,outgoing = True):
            """Return all (outgoing) edges incedent to vertex v in the Graph
            If graph is directed, optional parameters is used to requested incoming edges
            """
            adj = self._outgoing if outgoing else self._incoming
            for edge in adj[v].values():
                yield edge

            def insert_vertex(self, x=None):
                v = self.Vertex(x)
                self._outgoing[v] = {}
                if self._is_directed():
                    self._incoming[v] = {}
                return v
            
            def insert_edge(self, u,v,x=None):
                e=self.Edge(u,v,x)
                self._outgoing[u][v] = e
                self._incoming[v][u] = e

def DFS(G,u,discoveretd):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovored[v]=e
            DFS(g,v,discovered)
        
result={u:None}
DFS(g,u,result)