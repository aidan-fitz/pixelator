import numpy as np
from scipy.misc import imread, imsave
from sys import argv
from error import FileNotGivenError

fname_in = None
fname_out = None

args = iter(argv)

try:
    while True:
        nxt = args.next()
        if nxt == '-i':
            fname_in = args.next()
        elif nxt == '-o':
            fname_out = args.next()
        else:
            fname_in = nxt
except StopIteration:
    if fname_in is None:
        raise FileNotGivenError('I need a file name')
    elif fname_out is None:
        index = fname_in.rfind('.')
        fname_out = fname_in[:index] + '-pxl8d' + fname_in[index:]
