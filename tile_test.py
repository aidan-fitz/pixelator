#!/usr/bin/python3
#import different libraries
import numpy as np
from scipy.misc import imsave
from utils import *

pixel = np.asarray([0, 255, 255])

image = pixel_to_block(pixel, 240, 180)

imsave('output.png', image)
