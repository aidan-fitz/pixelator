import numpy as np
from utils import *

def avg_color(blocks): #it averages every color in each block structure the same
    # temp = upgrade(blocks[0][0])
    for row in range(len(blocks)):
        for column in range(len(blocks[row])):
            blocks[row][column] = avg_helper(blocks[row][column])

#helper function that averages a single block
def avg_helper(block):
    h, w, d = block.shape #sets a variable for the 3 dimensional array
    S = np.sum(block, axis=(0, 1), dtype = np.dtype(np.uint16)) #add all the elements in each row of the array or each column
    mean = S / (h*w) # returns an array of 3 numbers, avg red, g, and blue
    # Round, convert back to uint8, and tile to shape of original block
    return pixel_to_block(np.rint(mean).astype(np.dtype(np.uint8)), w, h)
