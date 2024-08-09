from collections import deque, defaultdict
graph = defaultdict(list)
def bfs(source, destination, n):
    queue = deque([source])
    #n is number of vertices in the graph
    visited = [False] * n
    while queue:
        curr_node = queue.popleft()
        visited[curr_node] = True
        if curr_node == destination:
            return True
        for neighbor in graph[curr_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False