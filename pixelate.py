#!/usr/bin/python3
#import different libraries
import numpy as np
from scipy.misc import imread, imsave
import cmd
from utils import *

#define variable
fin, fout = cmd.files()

print(fin)
print(fout)

image = imread(fin)

print(image.dtype)
print(image.shape)

blocks = chunk(image)

print(blocks[0][0].shape)
print(blocks[-1][-1].shape)

# to test chunk() and unchunk(), reconstruct the original image
reconstruct = unchunk(blocks)
imsave(fout, reconstruct)

def avg_color(blocks):
    temp = upgrade(blocks[0][0])
    # complete this function