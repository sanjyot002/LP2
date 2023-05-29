import sys

def dijkstra_mst(graph, src):
    num_vertices = len(graph)
    parent = [-1] * num_vertices  # Store the parent of each vertex in the MST
    dist = [sys.maxsize] * num_vertices
    dist[src] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        u = minDistance(dist, visited)
        visited[u] = True

        for v in range(num_vertices):
            if not visited[v] and graph[u][v] and graph[u][v] < dist[v]:
                parent[v], dist[v] = u, graph[u][v]

    return [(parent[v], v, graph[parent[v]][v]) for v in range(1, num_vertices)]

def minDistance(dist, visited):
    min_dist = sys.maxsize
    min_index = -1
    for v, d in enumerate(dist):
        if d < min_dist and not visited[v]:
            min_dist = d
            min_index = v
    return min_index

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
source = 0

mst = dijkstra_mst(graph, source)
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")
