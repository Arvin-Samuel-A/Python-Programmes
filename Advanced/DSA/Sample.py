"""import numpy as np

def dijkstra(WMat,s):
    (rows, cols,x) = WMat.shape

    infinity = np.max(WMat) *rows+1
    (visited, distance) = ({},{})

    for v in range(rows):
        (visited[v], distance [v]) = (False, infinity)

    distance [s] = 0

    for u in range(rows):
        nextd = min([distance [v] for v in range(rows) if not visited[v]])

        nextvlist = [v for v in range(rows) if not visited [v] and distance [v] == nextd]

        if nextvlist == []:
            break

        nextv = min(nextvlist)
        visited [nextv] = True
        print(nextv)
        for v in range(cols):
            if WMat [nextv,v,0] == 1 and (not visited[v]):
                
                distance [v] = min(distance [v], distance [nextv] + WMat [nextv,v,1])

    return(distance)

W_Adj_List={
    
    0:[(1, 10), (2, 80)],
    1:[(0, 10), (2, 6), (4, 20)],
    2:[(0, 80), (1, 6), (3, 70)],
    3:[(2, 70)],
    4:[(1, 20), (5, 50), (6, 5)],
    5:[(4, 50), (6, 10)],
    6:[(4, 5), (5, 10)]

}

num_vertices = len(W_Adj_List)

# Initialize a 3D NumPy array with zeros
W_Adj_Mat = np.zeros((num_vertices, num_vertices, 2), dtype=int)

# Fill in the adjacency matrix
for vertex, neighbors in W_Adj_List.items():
    for neighbor, weight in neighbors:
        W_Adj_Mat[vertex, neighbor, 0] = 1  # Indicates an edge exists
        W_Adj_Mat[vertex, neighbor, 1] = weight


print(dijkstra(W_Adj_Mat, 0))"""

from Bellman_Ford_Algorithm import Bellman_Ford_Algorithm_WAL as BFA

W_Adj_List={

    1: [(2, 10), (8, 8)],
    2: [(6, 2)],
    3: [(2, 1), (4, 1)],
    4: [(5, 3)],
    5: [(6, -1)],
    6: [(3, -2)],
    7: [(2, -4), (6, -1)],
    8: [(7, 1)]

}

print(BFA(W_Adj_List, 1))