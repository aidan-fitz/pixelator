#!/usr/bin/python3
#import different libraries
import numpy as np
from scipy.misc import imread, imsave
import cmd
from utils import *
from core import avg_color

#define variable
fin, fout = cmd.files()

print(fin)
print(fout)

image = imread(fin)

print(image.dtype)
print(image.shape)

blocks = chunk(image)

# Average the colors in place
avg_color(blocks)

# Reconstruct the original image with processed blocks
reconstruct = unchunk(blocks)
imsave(fout, reconstruct)
