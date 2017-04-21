import timeit
from collections import deque

class DAG:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)]
        self.visited = set()
        self.result = []

    def generateDAG(self):
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                self.matrix[i][j] = 1

    def dfs_recursive(self):
        for vertex in range(self.size):
            self.visit(vertex)
    def visit(self, vertex):
        if vertex not in self.visited:
            self.visited.add(vertex)
            for neighbor in range(self.size):
                if self.matrix[vertex][neighbor] == 1 and neighbor not in self.visited:
                    self.visit(neighbor)
            self.result.append(vertex)

    def dfs(self):
        stack = deque()
        visited = set()
        result = []
        vertex = -1
        while len(result) != self.size: #checking each vertex
            vertex += 1
            if vertex in visited:
                continue
            stack.append(vertex)
            while len(stack) != 0: #while there's something in the stack
                current = stack[-1]
                if current not in visited:
                    visited.add(current)
                    num = 0
                    for neighbor in range(self.size):
                        if self.matrix[current][neighbor] == 1 and neighbor not in visited:
                            stack.append(neighbor)
                            num += 1 #counting unvisited neighbors
                    if num == 0:
                        result.append(current)
                        stack.pop()
                else:
                    result.append(current)
                    stack.pop()
        return result

#topological sort
    def dfs_sort(self):
        return self.dfs()[::-1]

    def bfs_sort(self):
        result = []
        while len(result) != self.size:
            for col in range(self.size): #checking each vertex indegree
                if col not in result:
                    deg_in = 0
                    for row in range(self.size):
                        if self.matrix[row][col] == 1:
                            deg_in += 1
                    if deg_in == 0: #then remove every arc of this vertex
                        result.append(col)
                        self.matrix[col] = [0 for x in range(self.size)]
        return result

    def print_matrix(self):
        for i in range(self.size):
            print(self.matrix[i])


#sample adjacency matrix from  https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
size = 8
matrix = [[0,0,0,1,0,0,0,0],
          [0,0,0,1,1,0,0,0],
          [0,0,0,0,1,0,0,1],
          [0,0,0,0,0,1,1,1],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]
Graph = DAG(size)
Graph.matrix = matrix

print(Graph.dfs_sort())
print(Graph.bfs_sort())

# time tests
print("n-elements , dfs time [s] , bfs time [s]")
for n in range(2000,20001,2000):
    dfs = timeit.Timer('inst.dfs_sort()', 'from __main__ import DAG; inst=DAG({}); inst.generateDAG()'.format(n))
    bfs = timeit.Timer('inst.bfs_sort()', 'from __main__ import DAG; inst=DAG({}); inst.generateDAG()'.format(n))
    print(n,',', dfs.timeit(1), ',', bfs.timeit(1))




