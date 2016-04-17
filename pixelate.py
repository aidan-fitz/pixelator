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

blocks = chunk(image)

print(blocks[0][0].shape)
print(blocks[-1][-1].shape)

imsave(fout, blocks[len(blocks)//2][len(blocks[0])//2])
