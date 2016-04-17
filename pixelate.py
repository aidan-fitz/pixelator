#!/usr/bin/python3

import numpy as np
from scipy.misc import imread, imsave
import cmd

from utils import *

fin, fout = cmd.files()

print(fin)
print(fout)

image = imread(fin)

print(image.dtype)
print(image.shape)

maxrow = lambda row: min(row + 8, image.shape[0])
maxcol = lambda col: min(col + 8, image.shape[1])

blocks = [ \
            [[row, col, maxrow(row), maxcol(col)] \
            for row in range(0, image.shape[0], 8)] \
        for col in range(0, image.shape[1], 8)]

print(blocks[0][1])
print(blocks[1][1])
print(blocks[-1][-1])

'''
block = image[:8, :8]

print(block.shape)
'''
