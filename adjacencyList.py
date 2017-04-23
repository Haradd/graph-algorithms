import timeit
from collections import deque


class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_list = self.generateDAG()

    def generateDAG(self):
        adj_list = dict()
        for vertex in range(self.size):
            adj_list[vertex] = []
            for neighbor in range(vertex + 1, self.size):
                adj_list[vertex].append(neighbor)
        return  adj_list


    def dfs_sort(self):
        stack = deque()
        visited = set()
        result = []
        for vertex in range(self.size):
            if vertex in visited:
                continue
            stack.append(vertex)
            while len(stack) != 0:
                current = stack[-1]
                if current not in visited:
                    visited.add(current)
                    num = 0
                    for neighbor in self.adj_list[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            num += 1
                    if num == 0:
                        result.append(current)
                        stack.pop()
                else:
                    result.append(current)
                    stack.pop()
        return  result[::-1]

    def bfs_sort(self):
        result = []
        deg_in = {vertex : 0 for vertex in range(self.size)}
        for vertex in range(self.size):
            for neighbor in self.adj_list[vertex]:
                deg_in[neighbor] += 1

        to_remove = []
        for vertex in deg_in:
            if deg_in[vertex] == 0:
                result.append(vertex)
                to_remove.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    deg_in[neighbor] -= 1
        return result

    def print_list(self):
        print(self.adj_list)



#sample adjacency matrix from  https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
size = 8
MyGraph = Graph(size)
adj_list = {0:[3],
            1:[3,4],
            2:[4,7],
            3:[5,6,7],
            4:[6],
            5:[],
            6:[],
            7:[] }
MyGraph.adj_list = adj_list
print(MyGraph.generateDAG())
print(MyGraph.dfs_sort())
print(MyGraph.bfs_sort())



# time tests
print("n-elements , dfs time [s] , bfs time [s]")

for n in range(2000,20001,2000):
    dfs = timeit.Timer('inst.dfs_sort()',
                       'from __main__ import Graph; inst=Graph({})'.format(n))
    bfs = timeit.Timer('inst.bfs_sort()',
                       'from __main__ import Graph; inst=Graph({})'.format(n))
    print(n, ',', dfs.timeit(1), ',', bfs.timeit(1))


