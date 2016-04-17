import numpy as np

def upgrade(array):
    return array.astype(np.dtype(np.uint16))

def downgrade(array):
    return array.astype(np.dtype(np.uint8))

def chunk(array, dx = 16, dy = 16):
    if dx * dy >= 257:
        raise ValueError("Intermediate sums need to fit inside uint16!  A maximum of 257 uint8's can be added together, and %d * %d == %d won't fit." % (dx, dy, dx * dy))

    maxrow = lambda row: min(row + dy, array.shape[0])
    maxcol = lambda col: min(col + dx, array.shape[1])

    blocks = [ [ array[row : maxrow(row), col : maxcol(col)] for col in range(0, array.shape[1], dx) ] for row in range(0, array.shape[0], dy) ]
    return blocks
