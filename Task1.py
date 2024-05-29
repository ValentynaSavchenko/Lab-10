# 1.	Написати програму для обходу графа за алгоритмом пошуку в ширину:
# Савченко Валентина
class Graph:
    def __init__(self):
       self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = []

        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end='')

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
g = Graph()
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 1)
g.add_edge(3, 7)
g.add_edge(3, 6)
g.add_edge(3, 4)
g.add_edge(4, 3)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(4, 8)
g.add_edge(5, 4)
g.add_edge(5, 2)
g.add_edge(6, 3)
g.add_edge(6, 7)
g.add_edge(6, 4)
g.add_edge(7, 3)
g.add_edge(7, 6)
g.add_edge(7, 9)
g.add_edge(7, 8)
g.add_edge(8, 10)
g.add_edge(8, 4)
g.add_edge(8, 7)
g.add_edge(9, 7)
g.add_edge(10, 8)


print("Результат пошуку в ширину")
g.bfs(7)