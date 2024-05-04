class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, node):
        if node not in self.graph_dict:
            self.graph_dict[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.graph_dict[node1]:
            self.graph_dict[node1].append(node2)
        if node1 not in self.graph_dict[node2]:
            self.graph_dict[node2].append(node1)

    def exists(self, node):
        return node in self.graph_dict

    def get_neighbors(self, node):
        return self.graph_dict[node] if self.exists(node) else None

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(self.graph_dict[node])
        return visited

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(self.graph_dict[node])
        return visited