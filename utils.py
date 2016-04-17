import numpy as np

def upgrade(array):
    return array.astype(np.dtype(np.uint16))

def downgrade(array):
    return array.astype(np.dtype(np.uint8))

def chunk(array, dx = 16, dy = 16):
    if dx * dy >= 257:
        raise ValueError("Intermediate sums need to fit inside uint16!  A maximum of 257 uint8's can be added together.")
    stripes = np.array_split(array, dx, 1)
    print(stripes[0].shape)
    return stripes
