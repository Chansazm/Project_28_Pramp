from collections import defaultdict
class Graph:
    #create a graph based on an adjacency list representation of a graph using constructor
    def __init__(self):
        self.graph = defaultdict(list)
    
    #Method to add an edge to the graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    #Method to traverse the graph
    def Bfs(self,s):
        queue = []
        visited = [False] * (max(self.graph)+1)
        
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s,end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
#Driver function
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.Bfs(2)
