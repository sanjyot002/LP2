def color_graph(graph, num_colors):
    num_vertices = len(graph)
    coloring = [0] * num_vertices

    def is_safe(vertex, color):
        return all(coloring[adj_vertex] != color for adj_vertex in graph[vertex])

    def color_graph_util(vertex):
        if vertex == num_vertices:
            return True

        for color in range(1, num_colors + 1):
            if is_safe(vertex, color):
                coloring[vertex] = color
                if color_graph_util(vertex + 1):
                    return True
                coloring[vertex] = 0

        return False

    if not color_graph_util(0):
        print("No valid coloring exists.")
    else:
        print("Graph coloring:")
        for vertex, color in enumerate(coloring):
            print("Vertex", vertex, ":", "Color", color)

# Test the code with a sample graph
graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}
num_colors = 3

color_graph(graph, num_colors)