import heapq


def bestfirst(graph, heuristic, start, goal):
    li = []
    heapq.heappush(li, (heuristic[start], start))
    visited = set()
    previous_node = {start: None}
    
    while li:
        _, currentnode = heapq.heappop(li)
        if currentnode in visited:
            continue

        visited.add(currentnode)
        if currentnode == goal:
            break

        for n in graph[currentnode]:
            if n not in visited:
                priority = heuristic[n]
                heapq.heappush(li, (priority, n))
                previous_node[n] = currentnode
    
    path = []
    while currentnode:
        path.append(currentnode)
        currentnode = previous_node[currentnode]
    path.reverse()

    pathcost = 0
    for i in range(len(path) - 1):
        pathcost += graph[path[i]][path[i+1]]

    return path, pathcost

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    g_costs = {start: 0}
   
    while open_list:
        _, current = heapq.heappop(open_list)
       
        if current == goal:
            break
       
        for neighbor, cost in graph[current].items():
            tentative_g_cost = g_costs[current] + cost
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current
   
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    pathcost = g_costs[goal]
    return path, pathcost

def main():
    graph = {
        'arad': {'zerind': 75, 'timisora': 118, 'sibiu': 140},
        'zerind': {'arad': 75, 'oradea': 71},
        'timisora': {'arad': 118, 'lugoj': 111},
        'sibiu': {'arad': 140, 'oradea': 151, 'fagaras': 99, 'rimicu': 80},
        'fagaras': {'sibiu': 99, 'bucharest': 211},
        'bucharest': {'fagaras': 211, 'pitesti': 101},
        'pitesti': {'bucharest': 101, 'rimicu': 97},
        'oradea': {'zerind': 71, 'sibiu': 151},
        'dabaeu': {'rimicu': 80},
        'lugoj': {'timisora': 111},
        'rimicu': {'sibiu': 80, 'pitesti': 97, 'dabaeu': 80}
    }
    
    heuristic = {
        'arad': 366, 'zerind': 374, 'timisora': 329, 'sibiu': 253,
        'fagaras': 176, 'bucharest': 0, 'pitesti': 100, 'oradea': 380,
        'dabaeu': 256, 'lugoj': 244, 'rimicu': 193
    }
    
    start = 'arad'
    goal = 'bucharest'
    

    path_bfs, cost_bfs = bestfirst(graph, heuristic, start, goal)
    print(f"The Best-First Search path is {path_bfs}\nThe path cost is {cost_bfs}\n")
    

    path_astar, cost_astar = a_star_search(graph, start, goal, heuristic)
    print(f"The A* Search path is {path_astar}\nThe path cost is {cost_astar}\n")

if __name__ == "__main__":
    main()
