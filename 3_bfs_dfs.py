from collections import deque

def read_graph():
    graph = {}
    num_nodes = int(input("Enter Number of Nodes"))
    num_edges = int(input("Enter number of Edges"))

    print("Enter the edges as (A B)")
    for i in range(num_edges):
        u ,v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs(graph,start,goal):
    if start not in graph or goal not in graph:
        return []
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            result.append(vertex)
            return result
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return result

def dfs(graph,start,goal,visited=None):
    if visited is None:
        visited = set()
    if start not in graph or goal not in graph:
        return []
    visited.add(start)
    result = [start]

    if start == goal:
        return result
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph,neighbor,goal,visited)
            if goal in path:
                result.extend(path)
                return result
            
    return result
graph_ = read_graph()

start = input("Enter the starting node")
goal = input("Enter the goal node")

print("BFS Path",bfs(graph_,start,goal))
print("DFS Path",dfs(graph_,start,goal))
    