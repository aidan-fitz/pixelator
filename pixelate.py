#!/usr/bin/python3

import numpy as np
from scipy.misc import imread, imsave
import cmd

fin, fout = cmd.files()

print(fin)
print(fout)

image = imread(fin)

print(image.dtype)
print(image.shape)
