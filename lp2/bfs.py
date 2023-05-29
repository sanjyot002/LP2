from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)  # Print or process the current node here

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')




'''In this example, the graph is represented as a dictionary, where the keys represent the nodes, and the values are lists of neighboring nodes. The bfs function takes two parameters: the graph and the starting node.

The BFS algorithm uses a queue to keep track of nodes to visit. It starts by enqueueing the starting node. Then, it enters a loop where it dequeues a node from the front of the queue and visits it. For each neighbor of the current node, if the neighbor hasn't been visited before, it adds it to the queue.

The algorithm continues this process until the queue becomes empty, which means all reachable nodes have been visited. The print(node) line can be modified to perform any desired operations on each node instead of just printing it.

When you run this code, it will perform a BFS traversal starting from the 'A' node and print/process each visited node in breadth-first order.

Note that this implementation assumes that the graph is connected, meaning that every node is reachable from the starting node. If you're working with a disconnected graph, you may need to modify the code to handle multiple connected components.'''



'''The code imports the deque class from the collections module. A deque is a double-ended queue that allows efficient append and pop operations from both ends.

The bfs function takes two parameters: graph, which represents the graph as an adjacency list, and start, which is the starting vertex for the BFS traversal.

Inside the function, an empty set called visited is initialized to keep track of visited vertices.

A deque called queue is created with the starting vertex start enqueued.

The BFS traversal begins with a while loop that runs as long as the queue is not empty.

In each iteration, a vertex is dequeued from the left side of the queue using the popleft method.

The dequeued vertex node is checked if it has already been visited. If it hasn't, it is added to the visited set, and it can be printed or processed as desired.

The function then iterates over the neighbors of the node by accessing the corresponding list in the graph.

For each unvisited neighbor, it is added to the queue using the append method, so it can be visited in subsequent iterations.

The process continues until the queue becomes empty, indicating that all vertices have been visited.

In the example usage, an example graph graph is provided, represented as an adjacency list. The graph contains vertices 'A', 'B', 'C', 'D', 'E', and 'F', and the corresponding values in the dictionary are lists of their neighboring vertices.

Finally, the bfs function is called with the example graph and the starting vertex 'A'. This initiates the BFS traversal, printing or processing each visited vertex.

The BFS algorithm in this code ensures that vertices are visited in breadth-first order, exploring neighbors before moving on to vertices at the next level.'''






