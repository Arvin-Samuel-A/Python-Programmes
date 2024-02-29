import numpy as np

Edges, Component, Tree_Edges = [], {}, []

def WAM_Initialize(W_Adj_Mat : np.array):

    Edges.clear()
    Tree_Edges.clear()

    Len=len(W_Adj_Mat)

    for x in range(Len):

        for y in range(Len):

            if (W_Adj_Mat[x, y, 0]):

                Edges.append((W_Adj_Mat[x, y, 1], x, y))
        
        Component[x]=x

    Edges.sort()

    return


def WAL_Initialize(W_Adj_List : dict):

    Edges.clear()
    Tree_Edges.clear()

    for x in W_Adj_List:

        for v, w in W_Adj_List[x]:

            Edges.append((w, x, v))
        
        Component[x]=x

    Edges.sort()

    return


def Kruskal_Algorithm_WAM(W_Adj_Mat : np.array):

    WAM_Initialize(W_Adj_Mat)

    for w, x, y in Edges:

        if (Component[x]!=Component[y]):

            Tree_Edges.append((x, y))

            Var=Component[x]

            for x in range(len(W_Adj_Mat)):

                if (Component[x]==Var):

                    Component[x]=Component[y]

    return Tree_Edges


def Kruskal_Algorithm_WAL(W_Adj_List : dict):

    WAL_Initialize(W_Adj_List)

    for w, x, y in Edges:

        if (Component[x]!=Component[y]):

            Tree_Edges.append((x, y))

            Var=Component[x]

            for z in W_Adj_List:

                if Component[z]==Var:

                    Component[z]=Component[y]

    return Tree_Edges


if __name__=="__main__":

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

    W_Adj_Mat = np.zeros((num_vertices, num_vertices, 2), dtype=int)

    for vertex, neighbors in W_Adj_List.items():
        for neighbor, weight in neighbors:
            W_Adj_Mat[vertex, neighbor, 0] = 1
            W_Adj_Mat[vertex, neighbor, 1] = weight

    Kruskal_Algorithm_WAM(W_Adj_Mat)
    print(Tree_Edges)

    Kruskal_Algorithm_WAL(W_Adj_List)
    print(Tree_Edges)