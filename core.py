import numpy as np
from utils import *

def avg_color(blocks):
    temp = upgrade(blocks[0][0])
    # complete this function
#helper function that averages a single block
def avg_helper(block):
	h, w, d = block.shape #sets a variable for the 3 dimensional array
	S = np.sum(temp, axis=(0, 1), dtype = np.dtype(np.uint16))) #add all the elements in each row of the array or each column
	return S / (h*w) #returns an array of 3 numbers, avg red, g, and blue
