import numpy as np

def LCS(Word1 : str, Word2 : str):

    Len1 = len(Word1)
    Len2 = len(Word2)

    Table = np.zeros((Len1+1, Len2+1), dtype=np.int8)

    for x in range(Len1-1, -1, -1):

        for y in range(Len2-1, -1, -1):

            if (Word1[x] == Word2[y]):

                Table[x, y] = 1 + Table[x+1, y+1]

            else:

                Table[x, y] = max(Table[x, y+1], Table[x+1, y])
    
    return Table[0, 0]