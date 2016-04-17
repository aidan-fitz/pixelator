import numpy as np

'''
Converts byte (uint8) array to short (uint16) array
'''
def upgrade(array):
    return array.astype(np.dtype(np.uint16))

'''
Converts short array to byte array
'''
def downgrade(array):
    return array.astype(np.dtype(np.uint8))

'''
Returns a list[list] of blocks (rectangular regions of the image) in row-major order (a list of rows of blocks).
'''
def chunk(image, dx = 16, dy = 16):
    if dx * dy >= 257:
        raise ValueError("Intermediate sums need to fit inside uint16!  A maximum of 257 uint8's can be added together, and %d * %d == %d won't fit." % (dx, dy, dx * dy))

    # If the width and height are not multiples of dx and dy, don't go over the edge
    maxrow = lambda row: min(row + dy, image.shape[0])
    maxcol = lambda col: min(col + dx, image.shape[1])

    # List comprehension of slices
    blocks = [ [ image[row : maxrow(row), col : maxcol(col)] for col in range(0, image.shape[1], dx) ] for row in range(0, image.shape[0], dy) ]
    return blocks

'''
Combines a list[list] of blocks back into a single image.
'''
def unchunk(blocks):
    # First combine the blocks into horizontal stripes
    # MUST be done horizontally first or width mismatch errors will occur!
    stripes = [np.concatenate(row, axis = 1) for row in blocks]
    # Then combine the stripes vertically
    image = np.concatenate(stripes, axis = 0)
    return image

'''
Creates an x*y image of the pixel 'color' tiled across the plane.
'''
def pixel_to_block(color, x, y):
    return np.tile(color, (y, x, 1))
