def main():

    exampleGraph = [[0.0, 7.0, 0.0, 0.0, 1.0],
                    [7.0, 0.0, 6.0, 0.0, 5.0],
                    [0.0, 6.0, 0.0, 2.0, 3.0],
                    [0.0, 0.0, 2.0, 0.0, 4.0],
                    [1.0, 5.0, 3.0, 4.0, 0.0]]

    MST = primAlgorithm(5, exampleGraph)

    for i in range(5):
        s = ""
        for j in range(5):
            s += (str(MST[i][j]) + " ")
        print(s)

# PRIM'S ALGORITHM: Given a weighted connected undirected graph, compute a MST.
#      INPUT:   n: number of vertices
#               adj: adjacency matrix (2-dimensional array) with weights
#                   adj[0][3] (= adj[3][0]) is the weight of the edge between vertex 0 and vertex 3
#                   weight of an edge is a floating point number between [0.5, 1000]
#                   if there is no edge between i and j, adj[i][j] = 0
#      OUTPUT:  minTree: adjacency matrix (2-dimensional array) with boolean entries of the MST
#                   minTree[i][j] = True if the MST has an edge between the vertex i and j
#                   minTree[i][j] = False if the MST has no edge between the vertex i and j

def primAlgorithm(n, adj):
    minTree = [x[:] for x in [[False] * n] * n]
    dist_tree = [float("inf")] * n
    mst_cnt = 1
    mst = [0]*n
    u = 0
    mst[0] = 1
    dist_tree[0] = 0
    v = [-1]*n
    while mst_cnt < n:
        for node in range(n):
            if (adj[u][node] < dist_tree[node]) and (adj[u][node] > 0) and mst[node] == 0 :
                dist_tree[node] = adj[u][node]
                v[node] = u
        min_edge = float("inf")
        for node in range(n):
            if(mst[node] == 0 and dist_tree[node] < min_edge and dist_tree[node] > 0):
                u = node
                min_edge = dist_tree[node]
        dist_tree[u] = 0
        mst[u] = 1
        minTree[v[u]][u] = True
        minTree[u][v[u]] = True
        mst_cnt = mst_cnt + 1

    return minTree


if __name__ == "__main__":
    main()
