#A* search algorithm to find optimal path for given graph


from queue import PriorityQueue

def astar(graph, start, goal, heuristic):
    # Create a priority queue and enqueue the start node with priority 0
    queue = PriorityQueue()
    queue.put((0, start))

    # Create a dictionary to track the cost from start to each node
    cost = {start: 0}

    # Create a dictionary to track the optimal path from start to each node
    path = {start: None}

    while not queue.empty():
        # Dequeue the node with the lowest priority (lowest total cost)
        current_cost, current_node = queue.get()

        if current_node == goal:
            # Goal node reached, construct and return the optimal path
            return construct_path(path, goal)

        for neighbor, edge_cost in graph[current_node].items():
            # Calculate the cost from start to the neighbor through the current node
            total_cost = cost[current_node] + edge_cost

            if neighbor not in cost or total_cost < cost[neighbor]:
                # Update the cost and path for the neighbor
                cost[neighbor] = total_cost
                priority = total_cost + heuristic[neighbor]
                queue.put((priority, neighbor))
                path[neighbor] = current_node

    # No path found
    return None

def construct_path(path, goal):
    # Reconstruct the optimal path from the goal node to the start node
    current_node = goal
    optimal_path = [current_node]

    while path[current_node] is not None:
        current_node = path[current_node]
        optimal_path.append(current_node)

    # Reverse the path to get it from start to goal
    optimal_path.reverse()
    return optimal_path

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 5, 'E': 2},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 5},
    'E': {'B': 2, 'F': 1},
    'F': {'C': 4, 'E': 1}
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 4,
    'E': 2,
    'F': 0
}

start_node = 'A'
goal_node = 'F'

path = astar(graph, start_node, goal_node, heuristic)
if path is not None:
    print("Optimal path:", path)
else:
    print("No path found.")


    '''In this implementation, the graph is represented as a dictionary of dictionaries, where the keys of the outer dictionary represent the nodes, and the inner dictionaries represent the neighbors and the associated edge costs. The astar function takes four parameters: the graph, the start node, the goal node, and a heuristic dictionary.

The A* algorithm uses a priority queue to store the nodes to visit, prioritized based on the total cost, which is the sum of the cost from the start node to the current node and the heuristic estimate from the current node to the goal node. The algorithm starts by enqueuing the start node with a priority of 0.

The algorithm continues until the priority queue becomes empty or the goal node is reached. In each iteration, it dequeues the node with the lowest priority (lowest total cost) and checks if it's the goal node. If the goal node is reached, it reconstructs and returns the optimal path. Otherwise, it considers each neighbor of the current node, calculates the cost to reach the neighbor through the current node, and updates the cost and path if it's an improvement.

The construct_path function is used to reconstruct the optimal path from the goal node to the start node using the path dictionary.

In the example usage, the graph dictionary represents a simple undirected graph, and the heuristic dictionary provides heuristic estimates from each node to the goal node. The start_node and goal_node variables specify the start and goal nodes for the pathfinding problem. The astar function is called with these inputs, and the resulting optimal path is printed if it exists.

Note that this implementation assumes that the graph is connected, meaning that there is a valid path from the start node to the goal node. Additionally, the heuristic estimates must b'''




'''The code you provided implements the A* search algorithm for finding the optimal path from a start node to a goal node in a graph. A* is an informed search algorithm that uses a heuristic function to estimate the cost from each node to the goal.

Here's a breakdown of how the code works:

The astar function takes the following parameters: graph (the graph represented as a dictionary), start (the start node), goal (the goal node), and heuristic (the heuristic function).

It initializes a priority queue called queue and enqueues the start node with a priority of 0. The priority queue ensures that nodes with lower total cost are dequeued first.

Two dictionaries are created: cost and path. cost tracks the cost from the start node to each node, and path tracks the optimal path from the start node to each node.

The main loop continues until the queue is empty. In each iteration, it dequeues the node with the lowest priority (lowest total cost).

If the current node is the goal node, it calls the construct_path function to reconstruct the optimal path using the path dictionary and returns the path.

If the current node is not the goal node, it iterates over its neighbors and calculates the cost from the start node to each neighbor through the current node.

If the neighbor has not been visited before or the new cost is lower than the previous cost, it updates the cost and priority for the neighbor, enqueues the neighbor in the priority queue, and updates the path.

If no path is found (the queue becomes empty without reaching the goal node), it returns None to indicate that no path exists.

The construct_path function takes the path dictionary and the goal node as parameters. It reconstructs the optimal path from the goal node to the start node by following the nodes in the path dictionary.

The optimal path is reversed to get it from the start node to the goal node, and it is returned as a list.

In the example usage, a graph and a heuristic function are defined. The start node is set to 'A', and the goal node is set to 'F'. The astar function is called with these parameters, and if a path is found, it is printed. Otherwise, a "No path found" message is printed.'''