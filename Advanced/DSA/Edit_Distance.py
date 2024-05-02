import numpy as np

def ED(Word1 : str, Word2 : str):

    Len1 = len(Word1)
    Len2 = len(Word2)

    Table = np.zeros((Len1+1, Len2+1), dtype=np.int8)

    for x in range(Len1-1, -1, -1):

        Table[x, Len2] = Len1 - x

    for y in range(Len2-1, -1, -1):

        Table[Len1, y] = Len2 - y

    for x in range(Len1-1, -1, -1):

        for y in range(Len2-1, -1, -1):

            if (Word1[x] == Word2[y]):

                Table[x, y] = Table[x+1, y+1]

            else:

                Table[x, y] = 1 + min(Table[x+1, y+1], Table[x, y+1], Table[x+1, y])
    
    return Table[0, 0]