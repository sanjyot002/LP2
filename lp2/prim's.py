# Prim's Algorithm in Python


INF = 9999999
# number of vertices in graph
V = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + " - " + str(y) + " : " + str(G[x][y]))
    selected[y] = True
    no_edge += 1

# INF is a large constant used to represent infinity. It is initialized to 9999999.
# V represents the number of vertices in the graph and is set to 5 in this example.
# G is a 2D array (adjacency matrix) representing the graph. Each element G[i][j] represents the weight of the edge between vertex i and vertex j.
# selected is an array used to track the selected vertices. It is initially set to [0, 0, 0, 0, 0], indicating that no vertices are selected yet.

# no_edge is a variable that keeps track of the number of edges in the minimum spanning tree. It is initially set to 0.

# The first vertex, vertex 0, is chosen as the starting point and marked as selected by setting selected[0] = True.

# The code prints a header message indicating that the following output represents the edges and their weights.

# The code enters a while loop that continues until no_edge reaches V - 1, which is the number of edges in a minimum spanning tree with V vertices.
# Inside the loop, the code searches for the next minimum weight edge to add to the minimum spanning tree.

# It initializes minimum to INF and x and y to 0. These variables will store the indices of the vertices that form the minimum weight edge.

# The code iterates through the selected vertices (for i in range(V)) and for each selected vertex, it checks the unselected vertices (for j in range(V)) that are adjacent to it (G[i][j]).

# If an unselected vertex (not selected[j]) is adjacent to the selected vertex (G[i][j] is not 0), the code compares the weight of the edge (G[i][j]) with the current minimum weight (minimum).

# If the weight is smaller than the current minimum weight, it updates minimum, x, and y to store the new minimum weight and the corresponding vertex indices.

# After finding the minimum weight edge, the code prints the edge and its weight (str(x) + " - " + str(y) + " : " + str(G[x][y])).

# The vertex y is marked as selected by setting selected[y] = True.
# no_edge is incremented by 1 since a new edge has been added to the minimum spanning tree.

# The process continues until no_edge reaches V - 1, and the MST is complete.

# The code essentially performs a greedy approach, iteratively selecting the minimum weight edge from the available edges until the MST is formed. The selected vertices and edges are tracked using the selected array and no_edge variable. The result is printed as a list of edges with their corresponding weights.