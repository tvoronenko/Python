'''
You are given a list of projects and a list of dependencies( which is list of pair of projects, where the second
project is dependent on the first project). All of a project's dependencies must be 
built before the projects is. Find build order that will allow the projects to be built. If there is no valid build order, return
an error
Ex:
input
project: a,b,c,d,e,f
dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

output
f,e,a,b,d,c
'''

def find_build_order(projects, dependencies):
    graph = Graph (projects, dependencies)
    return order_projects(graph.get_nodes())
    
def order_projects(projects):
    stack = list()
    for project in projects:
        if project.get_state() == State.BLANK:
            if not do_dfs(project, stack):
                return null
    return stack
    
def do_dfs(project, stack):
    if project.get_state() == State.PARTIAL:
        return False#Cycle
    if project.get_state() == State.BLANK:
        project.set_state(State.PARTIAL)
        children = project.get_children()
        for child in children:
            if not do_dfs(child, stack):
                return False
        project.set_state(State.COMPLETE)
        stack.append(project)
    return True
  
def build_graph(projects, dependencies):
    """Build the graph, adding the edge (a, b) if b is dependent on a.
    Assumes a pair is listed in 'build order'. The pair (a, b) in dependencies
    indicates that b depends on a and a must be built before b."""
    graph = Graph()
    for project in projects:
        graph.create_node(project)
    for dependency in dependencies:
        first = dependency[0]
        second  = dependency[1]
        graph.add_edge(first, second)
    return graph

class Graph(Object):
  def __init__(self):
      self.nodes = []
      self.map_graph = {}
 
  def get_or_create_node(self, name):
      if name not in self.map_graph.keys():
          node = Project(name)
          self.nodes.append(node)
          self.map_graph[name] = node
      return self.map_graph[name]

  def add_edge(self, start_name, end_name):
      start = self.get_or_create_node(start_name)
      end = self.get_or_create_node(end_name)
      start.add_neighbor(end)
  
  def get_nodes(self):
      return self.nodes
  
from enum import Enum
class State(Enum):
...     COMPLETE = 1
...     PARTIAL = 2
...     BLANK = 3

class Project(Object):
    """Essentially equvalent to earlier solution, with state info added and
    dependency count removed"""
    def __init__(self, name, dependencies = 0, children = [], map_pr = {}):
        self.state = State.BLANK
        self.name = name
        self.children = children
        self.map_pr = map_pr
        self.dependencies = dependencies
  
    def add_neighbor(self, node):
        if node.get_name() not in self.map_pr:
            self.children.append(node)
            self.map_pr[node.get_name()] = node
            node.increment_dependecies()
    
    def increment_dependecies(self):
        self.dependencies += 1

    def decrement_dependecies(self):
        self.dependencies -= 1

    def get_name(self):
        return sef.name
  
    def get_children(self):
        return self.children
        
    def get_number_dependencies(self):
        return self.dependencies
    
    def get_state():
        return self.state
    
    def set_state(state):
        self.state = state
