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

stripes = chunk(image)

blocks = np.asarray([[[x, y] for x in range(0, image.shape[0], 8)] for y in range(0, image.shape[1], 8)])

print(blocks.shape)

print(blocks[0][0])
print(blocks[1][1])
print(blocks[-1][-1])

'''
block = image[:8, :8]

print(block.shape)
'''
