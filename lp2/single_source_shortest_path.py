import sys

def dijkstra(graph, source):
    # Number of vertices in the graph
    num_vertices = len(graph)

    # Initialize the distance array with maximum values
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0

    # Initialize the visited array
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Find the vertex with the minimum distance that has not been visited yet
        min_distance = sys.maxsize
        min_vertex = -1
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                min_vertex = v

        # Mark the vertex as visited
        visited[min_vertex] = True

        # Update the distance array for the adjacent vertices
        for v in range(num_vertices):
            if graph[min_vertex][v] > 0 and not visited[v]:
                new_distance = distance[min_vertex] + graph[min_vertex][v]
                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance

# Example usage:
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

source_vertex = 0

shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from source vertex", source_vertex)
for i in range(len(shortest_distances)):
    print("Vertex", i, ":", shortest_distances[i])




'''In this implementation, the graph variable represents the weighted graph. It is represented as a 2D list, where graph[i][j] represents the weight of the edge between vertices i and j. A weight of 0 indicates no edge between the vertices.

The dijkstra function takes the graph and the source vertex as input and returns a list distance that represents the shortest distances from the source vertex to all other vertices. The algorithm initializes the distance array with maximum values and sets the distance of the source vertex to 0.

The algorithm iteratively selects the vertex with the minimum distance that has not been visited yet. It marks the vertex as visited and updates the distance array for its adjacent vertices if a shorter path is found.

After the algorithm completes, the distance list contains the shortest distances from the source vertex to all other vertices. In the example usage, the dijkstra function is called with the graph variable and the source_vertex, and the resulting shortest distances are printed for each vertex.

Note that this implementation assumes that the graph is connected, meaning that there is a valid path between every pair of vertices. Additionally, it assumes that the graph is represented by an adjacency matrix.'''