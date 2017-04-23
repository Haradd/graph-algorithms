import timeit
from collections import deque


class Graph:
    def __init__(self, size):
        self.size = size
        self.edge_list = self.generateDAG()

    def generateDAG(self):
        edge_list = []
        for edge_out in range(self.size):
            for edge_in in range(edge_out+1, self.size):
                edge_list.append((edge_out, edge_in))
        return edge_list

#topological sorts
    def dfs_sort(self):
        stack = deque()
        visited = set()
        result = []
        for edge in range(self.size):
            if self.edge_list[edge][0] in visited:  # outgoing edge
                continue
            stack.append(self.edge_list[edge][0])
            while len(stack) != 0:
                current = stack[-1]
                if current not in visited:
                    visited.add(current)
                    for index in range(len(self.edge_list)):  # searching for edge index of currently checked vertex
                        if self.edge_list[index][0] == current:
                            edge_index = index
                            break
                    neighbors_num = 0
                    counter = 0
                    while self.edge_list[edge_index + counter][0] == current:  # pushing unvisited neighbors onto the stack
                        if self.edge_list[edge_index + counter][1] not in visited:
                            stack.append(self.edge_list[edge_index + counter][1])
                            neighbors_num += 1
                        try:  # break if there's edge_list index out of range
                            edge_list[edge_index + counter + 1]
                        except:
                            break
                        counter += 1
                    if neighbors_num == 0:
                        result.append(current)
                        stack.pop()
                else:
                    result.append(current)
                    stack.pop()
        return result[::-1]

    def bfs_sort(self):
        result = []
        #creating dict with indegrees
        deg_in = {vertex : 0 for vertex in range(self.size)}
        for edge_index in range(len(self.edge_list)):
                deg_in[self.edge_list[edge_index][1]] += 1

        for vertex in deg_in:
            if deg_in[vertex] == 0:
                result.append(vertex)
                for edge in self.edge_list:
                    if edge[0] == vertex:
                        deg_in[edge[1]] -= 1
        return result



#sample adjacency matrix from  https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
size = 8
edge_list = [(0,3),
             (1,3),
             (1,4),
             (2,4),
             (2,7),
             (3,5),
             (3,6),
             (3,7),
             (4,6)]
MyGraph = Graph(size)
MyGraph.edge_list = edge_list
print(MyGraph.dfs_sort())
print(MyGraph.bfs_sort())

# time tests
print("n-elements , dfs time [s] , bfs time [s]")

for n in range(200,20001,2000):
    dfs = timeit.Timer('inst.dfs_sort()',
                       'from __main__ import Graph; inst=Graph({})'.format(n))
    bfs = timeit.Timer('inst.bfs_sort()',
                       'from __main__ import Graph; inst=Graph({})'.format(n))
    print(n, ',', dfs.timeit(1), ',', bfs.timeit(1))
