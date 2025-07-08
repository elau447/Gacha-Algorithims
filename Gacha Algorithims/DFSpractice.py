def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)  # Process the node

            # Add unvisited neighbors to the stack (order matters for path exploration)
            for neighbor in reversed(graph[node]): # Reverse to maintain typical DFS order
                if neighbor not in visited:
                    stack.append(neighbor)

def dfs_recursive(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(start_node)  # Process the node (e.g., print it)

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example Graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal (Recursive):")
dfs_recursive(graph, 'A')
print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 'A')