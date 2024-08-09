#------------ITERATIVE------------
graph = {}
def dfs(start,end):
    stack = [start]
    seen = set()

    while stack:
        node = stack.pop()
        if node == end:
            return True

        if node in seen:
            continue
        seen.add(node)

        for neighbor in graph[node]:
            stack.append(neighbor)

    return False