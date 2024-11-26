import heapq

def best_first_search(graph, start, goal):
    pq = [(0, start)]  # Priority queue
    visited = set()
    while pq:
        cost, node = heapq.heappop(pq)
        if node == goal:
            print(f"Reached {goal}")
            return
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 6), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

best_first_search(graph, 'A', 'F')
