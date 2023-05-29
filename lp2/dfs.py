def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Print or process the current node here

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
'''graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}'''


graph = {
    '5' : ['3' , '7'],
    '3' : ['2' , '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

dfs(graph, '5')



'''In this example, the graph is represented as a dictionary, where the keys represent the nodes, and the values are lists of neighboring nodes. The dfs function takes three parameters: the graph, the starting node, and an optional visited set to keep track of visited nodes.

The DFS algorithm starts by adding the starting node to the visited set and prints/processes it. Then, for each neighbor of the current node, it recursively calls dfs if the neighbor hasn't been visited before.

When you run this code, it will perform a DFS traversal starting from the 'A' node and print/process each visited node. You can modify the print(start) line to perform any desired operations on each node instead of just printing it.

Note that this implementation assumes that the graph is connected, meaning that every node is reachable from the starting node. If you're working with a disconnected graph, you may need to modify the code to handle multiple connected components.'''